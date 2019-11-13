from application import db
from application.models import Base
from application.drinktypes.models import Drinktype
from sqlalchemy import Table

from sqlalchemy.sql import text

user_drink = Table('user_drink', Base.metadata, 
    db.Column('account_id', db.Integer, db.ForeignKey('account.id')), 
    db.Column('drink_id', db.Integer, db.ForeignKey('drink.id')))

ingredient_drink = Table('ingredient_drink', Base.metadata,
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')),
    db.Column('drink_id', db.Integer, db.ForeignKey('drink.id')),
    db.Column('amount', db.String(144)))

class Drink(Base):
    __tablename__ = "drink"

    name = db.Column(db.String(144), nullable=False)

    drinktype_id = db.Column(db.Integer, db.ForeignKey('drinktype.id'), nullable=False)
    
    instructions = db.Column(db.String(500), nullable=False)
    
    users = db.relationship("User", secondary=user_drink, back_populates='drinks', lazy='dynamic')

    ingredients = db.relationship("Ingredient", secondary=ingredient_drink, back_populates='drinks', lazy='dynamic')

    accepted = db.Column(db.Boolean(), nullable=False)

    def __init__(self, name):
        self.name = name

    def drinktype_name(self):
        return Drinktype.query.filter(Drinktype.id == self.drinktype_id).first().name

    def get_ingredients(drink_id):
        return Drink.query.get(drink_id).ingredients

    @staticmethod
    def search(keyword):
        stmt = text("SELECT drink.id, drink.name FROM drink" 
                    " INNER JOIN ingredient_drink"
                    " ON ingredient_drink.drink_id = drink.id" 
                    " INNER JOIN ingredient ON ingredient.id = ingredient_drink.ingredient_id" 
                    " WHERE (LOWER(drink.name) LIKE LOWER(:word) OR LOWER(ingredient.name) LIKE LOWER(:word))" 
                    " AND drink.accepted=:b GROUP BY drink.id LIMIT 5;").params(word = "%"+keyword+"%", b = True)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "ingredients": Drink.get_ingredients(row[0])})

        
        return response
