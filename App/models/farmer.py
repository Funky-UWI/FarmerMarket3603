from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    shop = db.relationship("shop")

    def __init__(self, username, password, first_name, last_name, email, phone):
        self.username = username
        self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.phone = phone

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

