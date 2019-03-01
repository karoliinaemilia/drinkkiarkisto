from flask import redirect, render_template, request, url_for

from flask_login import login_required, current_user

from application import app, db, login_required_with_role
from application.drinks.models import Drink
from application.auth.models import User
from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientToDrinkForm
from application.drinks.forms import DrinkForm, SearchForm

message = None

def set_message(newMessage):
    global message 
    message = newMessage

def get_message():
    global message
    message_help = message
    message = None
    return message_help

@app.route("/drinks/search", methods=["GET"])
@login_required
def drinks_search():
    return render_template("drinks/search.html", form = SearchForm())

@app.route("/drinks/search", methods=["POST"])
@login_required
def search_drink():
    form = SearchForm(request.form)

    drinks = Drink.search(form.keyword.data)

    if len(drinks) == 0:
        return render_template("drinks/search.html", form = SearchForm(), message = "Ei hakutuloksia")

    return render_template("drinks/search.html", form = SearchForm(), drinks = drinks)


@app.route("/drinks", methods=["GET"])
@login_required
def drinks_index():
    page = request.args.get('page', 1,  type=int)
    drinks = Drink.query.filter_by(accepted=True).paginate(page, 5, False)
    next_url = url_for('drinks_index', page = drinks.next_num) \
        if drinks.has_next else None
    prev_url = url_for('drinks_index', page = drinks.prev_num) \
        if drinks.has_prev else None
    return render_template("drinks/list.html", message = get_message(), drinks = drinks.items,
                           next_url = next_url, prev_url = prev_url)

@app.route("/drinks/new/")
@login_required
def drinks_form():
    return render_template("drinks/new.html", message = get_message(), form = DrinkForm())

@app.route("/drinks/<drink_id>/", methods=["GET"])
@login_required
def drinks_one(drink_id):
    return render_template("drinks/drink.html", form = DrinkForm(), drink = Drink.query.get(drink_id))

@app.route("/drink/delete/<drink_id>", methods=["POST"])
@login_required
def drink_delete(drink_id):

    d = Drink.query.get(drink_id)
    db.session().delete(d)
    db.session().commit()

    return redirect(url_for("drinks_index"))

@app.route("/drinks/", methods=["POST"])
@login_required
def drinks_create():
    form = DrinkForm(request.form)

    if not form.validate():
        return render_template("drinks/new.html", form = form)

    d = Drink(form.name.data)

    d.drinktype_id = form.drinktype.data

    d.instructions = form.instructions.data

    if current_user.is_admin():
        d.accepted = True
    else:
        d.accepted = False
    
    db.session().add(d)
    db.session().commit()

    def ingredient_query():
        ingredients = Ingredient.query.filter_by(accepted = True)
        ingredientlist = []
        for i in ingredients:
            ingredientlist.append((i.id, i.name))
        return ingredientlist
    
    form = IngredientToDrinkForm()
    form.name.choices = ingredient_query()
  
    return render_template("drinks/new.html", drink = d, ingredient_form = form)

@app.route("/drinks/<user_id>/<drink_id>", methods=["POST"])
@login_required
def add_favorite(drink_id, user_id):
    
    u = User.query.get(user_id)
    d = Drink.query.get(drink_id)

    if u.is_favorite(d):
        set_message("juoma on jo suosikeissasi")
        return redirect(url_for("drinks_index"))
        
    u.drinks.append(d)
    db.session().commit()

    return redirect(url_for("drinks_index"))

@app.route("/drinks/pending", methods=["GET"])
@login_required_with_role(role="ADMIN")
def drinks_pending():

    drinkpage = request.args.get('drinkpage', 1,  type=int)
    drinks = Drink.query.filter_by(accepted=False).paginate(drinkpage, 2, False)
    drink_next_url = url_for('drinks_pending', drinkpage = drinks.next_num) \
        if drinks.has_next else None
    drink_prev_url = url_for('drinks_pending', drinkpage = drinks.prev_num) \
        if drinks.has_prev else None

    ingredientpage = request.args.get('ingredientpage', 1,  type=int)
    ingredients = Ingredient.query.filter_by(accepted=False).paginate(ingredientpage, 2, False)
    ingredient_next_url = url_for('drinks_pending', ingredientpage = ingredients.next_num) \
        if ingredients.has_next else None
    ingredient_prev_url = url_for('drinks_pending', ingredientpage = ingredients.prev_num) \
        if ingredients.has_prev else None

    return render_template("drinks/pending.html", drinks = drinks.items, ingredients = ingredients.items, 
                            drink_next_url = drink_next_url, drink_prev_url = drink_prev_url, 
                            ingredient_next_url = ingredient_next_url, ingredient_prev_url = ingredient_prev_url)

@app.route("/drinks/message", methods=["GET"])
@login_required
def drinks_message():
    if current_user.is_admin():
        set_message("Drinkki on lisäty onnistuneesti")
    else:
        set_message("Kiitos ehdotuksestasi!")

    return redirect(url_for("drinks_index"))


@app.route("/drink/accept/<drink_id>", methods=["POST"])
@login_required_with_role(role="ADMIN")
def accept_drink(drink_id):

    d = Drink.query.get(drink_id)

    d.accepted = True

    db.session().commit()

    return redirect(url_for("drinks_pending"))

@app.route("/drink/pending/decline/<drink_id>", methods=["POST"])
@login_required_with_role(role="ADMIN")
def decline_drink(drink_id):

    d = Drink.query.get(drink_id)

    db.session().delete(d)
    db.session().commit()

    return redirect(url_for("drinks_pending"))