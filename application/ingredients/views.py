from flask import redirect, render_template, request, url_for

from flask_login import login_required, current_user

from application import app, db, login_required_with_role
from application.ingredients.models import Ingredient
from application.drinks.models import Drink, ingredient_drink
from application.ingredients.forms import IngredientForm, IngredientToDrinkForm

message = None

def set_message(newMessage):
    global message 
    message = newMessage

def get_message():
    global message
    message_help = message
    message = None
    return message_help

@app.route("/ingredients/new/")
@login_required
def ingredients_form():
    page = request.args.get('page', 1,  type=int)
    ingredients = Ingredient.query.filter_by(accepted=True).paginate(page, 5, False)
    next_url = url_for('ingredients_form', page = ingredients.next_num) \
        if ingredients.has_next else None
    prev_url = url_for('ingredients_form', page = ingredients.prev_num) \
        if ingredients.has_prev else None
    return render_template("ingredients/new.html", message = get_message(), ingredients = ingredients.items,
                           next_url = next_url, prev_url = prev_url, form = IngredientForm())

@app.route("/ingredients/", methods=["POST"])
@login_required
def ingredients_create():
    form = IngredientForm(request.form)

    i = Ingredient(form.name.data)
    

    if current_user.is_admin():
        i.accepted = True
        set_message("ainesosa lisätty")
    else:
        i.accepted = False
        set_message("kiitos ehdotuksestasi!")
    
    db.session().add(i)
    db.session().commit()
    
    form = IngredientForm()
    return redirect(url_for("ingredients_form"))

@app.route("/ingredient/accept/<ingredient_id>", methods=["POST"])
@login_required_with_role(role="ADMIN")
def accept_ingredient(ingredient_id):

    i = Ingredient.query.get(ingredient_id)

    i.accepted = True

    db.session().commit()

    return redirect(url_for("drinks_pending"))

@app.route("/ingredient/pending/decline/<ingredient_id>", methods=["POST"])
@login_required_with_role(role="ADMIN")
def decline_ingredient(ingredient_id):

    i = Ingredient.query.get(ingredient_id)

    db.session().delete(i)
    db.session().commit()

    return redirect(url_for("drinks_pending"))

@app.route("/drink/ingredient/<drink_id>", methods=["POST"])
@login_required
def add_ingredient(drink_id):
    form = IngredientToDrinkForm(request.form)

    i = Ingredient.query.get(form.name.data)
    d = Drink.query.get(drink_id)

    def ingredient_query():
        ingredients = Ingredient.query.filter_by(accepted = True)
        ingredientlist = []
        for i in ingredients:
            ingredientlist.append((i.id, i.name))
        return ingredientlist

    nextform = IngredientToDrinkForm()
    nextform.name.choices = ingredient_query()

    if i.is_ingredient(d):
        return render_template("drinks/new.html", message="ainesosa on jo lisätty", drink=d, ingredients = d.ingredients, ingredient_form=nextform )
        
    statement = ingredient_drink.insert().values(drink_id=drink_id, ingredient_id=i.id, amount= form.amount.data)
    db.session().execute(statement)
    db.session().commit()

    return render_template("drinks/new.html", drink = d, ingredients = d.ingredients, ingredient_form = nextform)

@app.route("/ingredient/delete/<ingredient_id>", methods=["POST"])
@login_required_with_role(role="ADMIN")
def ingredient_delete(ingredient_id):

    i = Ingredient.query.get(ingredient_id)
    db.session().delete(i)
    db.session().commit()

    return redirect(url_for("ingredients_form"))
