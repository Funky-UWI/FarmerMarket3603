from App.models import Order
from App.database import db

def get_all_orders():
    orders = Order.query.all()
    return orders

def get_all_orders_json():
    orders = Order.query.all()
    return [order.toJSON() for order in orders]

# def get_all_orders_by_user():


def create_order(listing, cart):
    order = Order(listing=listing, cart=cart)
    db.session.add(order)
    db.session.commit()
    return order

def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()
    return