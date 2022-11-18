from App.models import Order
from App.database import db
from App.controllers.listing import get_listings_by_shop 

def get_all_orders():
    orders = Order.query.all()
    return orders

def get_all_orders_json():
    orders = Order.query.all()
    return [order.toJSON() for order in orders]

def get_all_orders_by_shop(shop_id):
    # SELECT order.listing.id WHERE order.listing.shop_id = shop_id
    listings = get_listings_by_shop(shop_id)
    orders_all = get_all_orders()
    # order_ids = [order.listing.id for order in orders_all]
    listing_ids = [listing['id'] for listing in listings]
    # orders = [listing for listing in listings if listing['id'] in order_ids]
    orders = [order.toJSON() for order in orders_all if order.listing.id in listing_ids]
    # orders = [order.toJSON() for order in orders_all]
    return orders


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