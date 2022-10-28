from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False)
    description = db.Column(db.String(400), nullable=False)
    address1 = db.Column(db.String(200), nullable=False)
    address2 = db.Column(db.String(200), nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey("farmer.id"))
    farmer = db.relationship("Farmer", back_populates="shop")

    def __init__(self, name, description, address1, address2, farmer_id):
        self.name = name
        self.description = description
        self.address1 = address1
        self.address2 = address2
        self.farmer_id = farmer_id

    def toJSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address1': self.address1,
            'address2': self.address2,
        }