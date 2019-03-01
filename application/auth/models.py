from application import db
from application.models import Base
from application.drinks.models import user_drink

from sqlalchemy.sql import text

class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144), nullable=False)

    drinks = db.relationship("Drink", secondary=user_drink, back_populates='users', lazy='dynamic')

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return [self.role]
    
    def is_admin(self):
        return self.role == "ADMIN"

    def is_favorite(self, drink):
        return self.drinks.filter(user_drink.c.drink_id == drink.id).count() > 0

    @staticmethod
    def find_favorites(user_id):
        stmt = text("SELECT drink.name FROM drink"
                    " INNER JOIN user_drink ON user_drink.drink_id = drink.id"
                    " AND user_drink.account_id = :id GROUP BY drink.name").params(id = user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})
        
        return response

    @staticmethod
    def find_favorite_ingredients(user_id):
        stmt = text("SELECT COUNT(ingredient.id) AS favorites, ingredient.name FROM Ingredient"
                    " INNER JOIN ingredient_drink ON ingredient.id = ingredient_drink.ingredient_id" 
                    " INNER JOIN drink ON ingredient_drink.drink_id = drink.id"
                    " INNER JOIN user_drink ON user_drink.drink_id = drink.id"
                    " INNER JOIN account on account.id = user_drink.account_id"
                    " WHERE account_id = :id GROUP BY ingredient.name"
                    " ORDER BY favorites DESC limit 3").params(id = user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"frequency":row[0], "ingredient":row[1]})

        return response