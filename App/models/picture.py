from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey("listing.id"))
    url =  db.Column(db.String, nullable=False)

    listing = db.relationship("Listing")
    

    def __init__(self, listing_id, url):
        self.listing_id = listing_id
        self.url = url

    def toJSON(self):
        return{
            'id': self.id,
            'listing_id': self.listing_id,
            'url': self.url,
        }