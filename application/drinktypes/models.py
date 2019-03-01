from application import db
from application.models import Base

class Drinktype(Base):
    __tablename__ = "drinktype"

    name = db.Column(db.String(144), nullable=False)

    drinks = db.relationship("Drink", backref='drinktype', lazy='dynamic')

    def __init__(self, name):
        self.name = name