from App.models import Order
from App.database import db

def get_all_orders():
    orders = Order.query.all()
    return orders

def get_all_orders_json():
    orders = Order.query.all()
    return [order.toJSON() for order in orders]

def create_order(name, ask_price, unit, shop_id):
    order = Order(name=name, ask_price=ask_price, unit=unit, shop_id=shop_id)
    db.session.add(order)
    db.session.commit()
    return order

def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()
    return