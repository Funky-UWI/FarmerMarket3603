from App.models import Farmer
from App.database import db

def create_user(username, password):
    newuser = Farmer(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return Farmer.query.filter_by(username=username).first()

def get_user(id):
    return Farmer.query.get(id)

def get_all_users():
    return Farmer.query.all()

def get_all_users_json():
    users = Farmer.query.all()
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    