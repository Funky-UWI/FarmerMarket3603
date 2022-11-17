from App.database import db
from sqlalchemy.dialects.postgresql import UUID

class Cart(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key=True)
    # session_id = db.Column(UUID(as_uuid=True), unique=True)
    session_id = db.Column(db.String, unique=True)
    order = db.relationship("Order", back_populates="cart")

    def __init__(self, session_id):
        self.session_id = session_id

    def get_total(self):
        total = 0.0
        for order in self.order:
            total += order.listing.ask_price
        return total

    def toJSON(self):
        return{
            'id': self.id,
            'session_id': self.session_id,
            'orders': [order.toJSON() for order in self.order],
            'total': self.get_total()
        }