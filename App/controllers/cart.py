from App.models import Cart
from App.database import db

def create_cart(id):
    cart = Cart(id)
    db.session.add(cart)
    db.session.commit()
    return cart

def get_cart_by_session(session_id):
    cart = Cart.query.filter_by(session_id=str(session_id)).first()
    return cart

def get_cart(id):
    cart = Cart.query.get(id)
    return cart

def get_cart_by_current_user(current_user, session):
    cart = None
    if current_user.is_authenticated:
        cart = get_cart_by_session(current_user.id)
    else:
        cart = get_cart_by_session(session['uuid'])
    return cart