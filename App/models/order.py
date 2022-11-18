from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    cart = db.relationship("Cart", back_populates="order")
    customer_first_name =  db.Column(db.String, nullable=True)
    customer_last_name =  db.Column(db.String, nullable=True)
    customer_email =  db.Column(db.String, nullable=True)
    customer_phone =  db.Column(db.String, nullable=True)
    # city should be choice column
    customer_city =  db.Column(db.String, nullable=True)
    customer_address1 =  db.Column(db.String, nullable=True)
    customer_address2 =  db.Column(db.String, nullable=True)
    isDelivery =  db.Column(db.Boolean, nullable=True)
    delivery_date_time =  db.Column(db.DateTime, nullable=True)


    listing_id = db.Column(db.Integer, db.ForeignKey("listing.id"))
    listing = db.relationship("Listing")

    # def __init__(self, listing, cart, customer_first_name, customer_last_name, customer_email, customer_phone, customer_city, customer_address1, customer_address2, isDelivery, delivery_date_time):
    #     self.customer_first_name = customer_first_name
    #     self.customer_last_name = customer_last_name
    #     self.customer_email = customer_email
    #     self.customer_phone = customer_phone
    #     self.customer_city = customer_city
    #     self.customer_address1 = customer_address1
    #     self.customer_address2 = customer_address2
    #     self.isDelivery = isDelivery
    #     self.delivery_date_time = delivery_date_time
    #     self.cart = cart
    #     self.listing = listing

    def __init__(self, listing, cart):
        self.cart = cart
        self.listing = listing

    # def toJSON(self):
    #     return{
    #         'customer_first_name': self.customer_first_name,
    #         'customer_last_name': self.customer_last_name,
    #         'customer_email': self.customer_email,
    #         'customer_phone': self.customer_phone,
    #         'customer_city': self.customer_city,
    #         'customer_address1': self.customer_address1,
    #         'customer_address2': self.customer_address2,
    #         'isDelivery': self.isDelivery,
    #         'delivery_date_time': self.delivery_date_time,
    #     }

    def toJSON(self):
        return{
            'cart_id': self.cart_id,
            'listing': self.listing.toJSON()
        }