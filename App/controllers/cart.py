from App.models import Cart
from App.database import db

def create_cart(id):
    cart = Cart(id)
    db.session.add(cart)
    db.session.commit()
    return cart

def get_cart_by_session(session_id):
    cart = Cart.query.filter_by(session_id=session_id).first()
    return cart

def get_cart(id):
    cart = Cart.query.get(id)
    return cart