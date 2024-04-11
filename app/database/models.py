from . import db

class Conversion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    currency_from = db.Column(db.String(3), nullable=False)
    currency_to = db.Column(db.String(3), nullable=False)
    rate = db.Column(db.Float, nullable=False)
