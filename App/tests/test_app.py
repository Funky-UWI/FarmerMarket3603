import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import Farmer
from App.controllers import (
    create_user,
    get_all_users_json,
    authenticate,
    get_user,
    get_user_by_username,
    update_user
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = Farmer("bob", "bobpass", "bob", "loblaw", "bobloblaw@gmail.com", "3161135")
        assert user.username == "bob"

    # pure function no side effects or integrations called
    def test_toJSON(self):
        user = Farmer("bob", "bobpass", "bob", "loblaw", "bobloblaw@gmail.com", "3161135")
        user_json = user.toJSON()
        self.assertDictEqual(user_json, {
            "id":None, 
            "username":"bob", 
            "first_name":"bob", 
            "last_name":"loblaw",
            "email":"bobloblaw@gmail.com",
            "phone":"3161135"
        })
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = Farmer("bob", password, "bob", "loblaw", "bobloblaw@gmail.com", "3161135")
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = Farmer("bob", password, "bob", "loblaw", "bobloblaw@gmail.com", "3161135")
        assert user.check_password(password)

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


def test_authenticate():
    user = create_user("bob", "bobpass", "bob", "loblaw", "bobloblaw@gmail.com", "3161135")
    assert authenticate("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass", "rick", "loblaw", "rickloblaw@gmail.com", "3161135")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([
            {
                "id":1, 
            "username":"bob", 
            "first_name":"bob", 
            "last_name":"loblaw",
            "email":"bobloblaw@gmail.com",
            "phone":"3161135"
            }, 
            {
                "id":2, 
            "username":"rick", 
            "first_name":"rick", 
            "last_name":"loblaw",
            "email":"rickloblaw@gmail.com",
            "phone":"3161135"
            }
        ], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"
