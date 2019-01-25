from application import db

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    drinkType = db.Column(db.String(144), nullable=False)


    def __init__(self, name, drinkType):
        self.name = name
        self.drinkType = drinkType