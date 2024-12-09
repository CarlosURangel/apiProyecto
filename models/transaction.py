from utils.db import db
from datetime import datetime

class MinisuperTransaction(db.Model):
    __bind_key__ = None
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Float(15), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False)
    response = db.Column(db.String(100), nullable=True, default="Pending")
    commission = db.Column(db.Float, nullable=False)

    def __init__(self, phone_number, amount, response= "Pending", commission=0.0):
        self.phone_number = phone_number
        self.amount = amount
        self.response = response
        self.commission = commission

class TelcelTransaction(db.Model):
    __bind_key__ = 'telcel'
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False)
    response = db.Column(db.String(100), nullable=True, default="Pending")
    commission = db.Column(db.Float, nullable=False)

    def __init__(self, phone_number, amount, response="Pending", commission=0.0):
        self.phone_number = phone_number
        self.amount = amount
        self.response = response
        self.commission = commission


class DalefonTransaction(db.Model):
    __bind_key__ = 'dalefon'
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False)
    response = db.Column(db.String(100), nullable=True, default="Pending")
    commission = db.Column(db.Float, nullable=False)

    def __init__(self, phone_number, amount, response="Pending", commission=0.0):
        self.phone_number = phone_number
        self.amount = amount
        self.response = response
        self.commission = commission


class BaitTransaction(db.Model):
    __bind_key__ = 'bait'
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False)
    response = db.Column(db.String(100), nullable=True, default="Pending")
    commission = db.Column(db.Float, nullable=False)

    def __init__(self, phone_number, amount, response="Pending", commission=0.0):
        self.phone_number = phone_number
        self.amount = amount
        self.response = response
        self.commission = commission