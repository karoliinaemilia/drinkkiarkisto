from application import app, db
from flask import redirect, render_template, request, url_for
from application.drinks.models import Drink

@app.route("/drinks", methods=["GET"])
def drinks_index():
    return render_template("drinks/list.html", drinks = Drink.query.all())

@app.route("/drinks/new/")
def drinks_form():
    return render_template("drinks/new.html")

@app.route("/drinks/<drink_id>/", methods=["GET"])
def drinks_one(drink_id):
    return render_template("drinks/drink.html", drink = Drink.query.get(drink_id))

@app.route("/drinks/<drink_id>/", methods=["POST"])
def drinks_change(drink_id):

    d = Drink.query.get(drink_id)
    d.drinkType = request.form.get("drinkType")
    db.session().commit()

    return render_template("drinks/drink.html", drink = Drink.query.get(drink_id))

@app.route("/drinks/", methods=["POST"])
def drinks_create():
    d = Drink(request.form.get("name"), request.form.get("drinkType"))
    
    db.session().add(d)
    db.session().commit()
  
    return redirect(url_for("drinks_index"))