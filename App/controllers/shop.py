from App.models import Farmer
from App.database import db
from App.models.shop import Shop

def create_shop(name, description, address1, address2, farmer_id):
    newshop = Shop(name=name, description=description, address1=address1, address2=address2, farmer_id=farmer_id)
    db.session.add(newshop)
    db.session.commit()
    return newshop

def get_all_shops():
    return Shop.query.all()

def get_all_shops_json():
    shops = Shop.query.all()
    return [shop.toJSON() for shop in shops]

def get_shop(id):
    return Shop.query.get(id)