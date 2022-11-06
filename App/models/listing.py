from enum import unique
from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False)
    ask_price = db.Column(db.Float, nullable=False)
    # unit will be a choice column
    unit = db.Column(db.String(10), nullable=False) 
    shop_id = db.Column(db.Integer, db.ForeignKey("shop.id"))
    shop = db.relationship("Shop")
    picture = db.relationship("Picture", back_populates="listing")

    def __init__(self, name, ask_price, unit, shop):
        self.name = name
        self.ask_price = ask_price
        self.unit = unit
        self.shop = shop

    def toJSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'ask_price': self.ask_price,
            'unit': self.unit,
            'shop': self.shop.toJSON()
        }