from application import db
from application.models import Base
from application.drinks.models import ingredient_drink

from sqlalchemy.sql import text

class Ingredient(Base):
    __tablename__ = "ingredient"

    name = db.Column(db.String(144), nullable=False)

    accepted = db.Column(db.Boolean(), nullable=False)
    drinks = db.relationship("Drink", secondary=ingredient_drink, back_populates='ingredients', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def is_ingredient(self, drink):
        return self.drinks.filter(ingredient_drink.c.drink_id == drink.id).count() > 0
    
    @staticmethod
    def get_amount(self, drink):
        stmt = text("SELECT amount FROM ingredient_drink"
                    " WHERE ingredient_drink.drink_id = :id "
                    " AND ingredient_drink.ingredient_id = :id2").params(id = drink.id, id2 = self.id)
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]