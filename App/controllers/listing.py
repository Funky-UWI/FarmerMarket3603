from App.models import Listing
from App.database import db

def get_all_listings():
    listings = Listing.query.all()
    return listings

def get_all_listings_json():
    listings = Listing.query.all()
    return [listing.toJSON() for listing in listings]

def create_listing(name, ask_price, unit, shop, description):
    listing = Listing(name=name, ask_price=ask_price, unit=unit, shop=shop, description=description)
    db.session.add(listing)
    db.session.commit()
    return listing

def delete_listing(id):
    listing = Listing.query.get(id)
    db.session.delete(listing)
    db.session.commit()
    return