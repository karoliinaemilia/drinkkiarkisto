from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.drinks.models import Drink
from application.drinks.forms import DrinkForm

@app.route("/drinks", methods=["GET"])
@login_required
def drinks_index():
    return render_template("drinks/list.html", drinks = Drink.query.all())

@app.route("/drinks/new/")
@login_required
def drinks_form():
    return render_template("drinks/new.html", form = DrinkForm())

@app.route("/drinks/<drink_id>/", methods=["GET"])
@login_required
def drinks_one(drink_id):
    return render_template("drinks/drink.html", form = DrinkForm(), drink = Drink.query.get(drink_id))

@app.route("/drinks/<drink_id>/", methods=["POST"])
@login_required
def drinks_change(drink_id):

    form = DrinkForm(request.form)

    if not form.validate():
        return render_template("drinks/drink.html", form = form, drink =  Drink.query.get(drink_id))

    d = Drink.query.get(drink_id)
    d.name = request.form.get("name")
    d.drinktype = request.form.get("drinktype")
    db.session().commit()

    return render_template("drinks/drink.html", form = form, drink = Drink.query.get(drink_id))

@app.route("/drink/delete/<drink_id>", methods=["POST"])
@login_required
def drink_delete(drink_id):

    d = Drink.query.get(drink_id)
    db.session().delete(d)
    db.session().commit()

    return render_template("drinks/list.html", drinks = Drink.query.all())

@app.route("/drinks/", methods=["POST"])
@login_required
def drinks_create():
    form = DrinkForm(request.form)

    if not form.validate():
        return render_template("drinks/new.html", form = form)

    d = Drink(form.name.data, form.drinktype.data)
    
    db.session().add(d)
    db.session().commit()
  
    return redirect(url_for("drinks_index"))