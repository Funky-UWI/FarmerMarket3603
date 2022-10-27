from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_first_name =  db.Column(db.String, nullable=False)
    customer_last_name =  db.Column(db.String, nullable=False)
    customer_email =  db.Column(db.String, nullable=False)
    customer_phone =  db.Column(db.String, nullable=False)
    # city should be choice column
    customer_city =  db.Column(db.String, nullable=False)
    customer_address1 =  db.Column(db.String, nullable=False)
    customer_address2 =  db.Column(db.String, nullable=False)
    isDelivery =  db.Column(db.Boolean, nullable=False)
    delivery_date_time =  db.Column(db.DateTime, nullable=False)


    listing_id = db.Column(db.Integer, db.ForeignKey("listing.id"))
    listing = db.relationship("listing")

    def __init__(self, customer_first_name, customer_last_name, customer_email, customer_phone, customer_city, customer_address1, customer_address2, isDelivery, delivery_date_time):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name
        self.customer_email = customer_email
        self.customer_phone = customer_phone
        self.customer_city = customer_city
        self.customer_address1 = customer_address1
        self.customer_address2 = customer_address2
        self.isDelivery = isDelivery
        self.delivery_date_time = delivery_date_time

    def toJSON(self):
        return{
            'customer_first_name': self.customer_first_name,
            'customer_last_name': self.customer_last_name,
            'customer_email': self.customer_email,
            'customer_phone': self.customer_phone,
            'customer_city': self.customer_city,
            'customer_address1': self.customer_address1,
            'customer_address2': self.customer_address2,
            'isDelivery': self.isDelivery,
            'delivery_date_time': self.delivery_date_time,
        }