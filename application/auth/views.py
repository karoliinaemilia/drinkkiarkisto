from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db, login_required_with_role
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm, PasswordForm

@app.route("/")
def index():
    return redirect(url_for("auth_login"))

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Incorrect username or password")

    login_user(user)
    return redirect(url_for("drinks_search"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/signup", methods = ["GET", "POST"])
def auth_signup():
    if request.method == "GET":
        return render_template("auth/signupform.html", form = SignupForm())
    
    form = SignupForm(request.form)

    if not form.validate():
        return render_template("auth/signupform.html", form = form)

    u = User(form.name.data, form.username.data, form.password.data)
    
    u.role = "REGULAR"
    db.session().add(u)
    db.session().commit()

    return render_template("auth/loginform.html", form = LoginForm())

@app.route("/users/<user_id>/", methods=["GET"])
@login_required
def user_profile(user_id):
    if int(current_user.id) == int(user_id):
        return render_template("auth/user.html", form = PasswordForm(), user = User.query.get(user_id), message = get_message(), favorite_ingredients = User.find_favorite_ingredients(user_id), favorite_drinks = User.find_favorites(user_id))
        
    return redirect(url_for("drinks_index"))
        

@app.route("/user/delete/<user_id>", methods=["POST"])
@login_required
def user_delete(user_id):

    u = User.query.get(user_id)
    db.session().delete(u)
    db.session().commit()

    logout_user()
    return redirect(url_for("drinks_index"))

@app.route("/user/makeadmin/<user_id>", methods=["POST"])
@login_required_with_role(role="ADMIN")
def make_admin(user_id):

    u = User.query.get(user_id)
    u.role = "ADMIN"
    
    db.session().commit()

    return redirect(url_for("users_index"))

@app.route("/user/<user_id>/", methods=["POST"])
@login_required
def password_change(user_id):

    form = PasswordForm(request.form)

    if not form.validate():
        return render_template("auth/user.html", form = form, user = User.query.get(user_id))

    u = User.query.get(user_id)

    if not u.password == form.password.data:
        return render_template("auth/user.html", form=form, user=u, error="Vanha salasana väärin")

    u.password = form.new_password.data
    db.session().commit()

    set_message("Salasana vaihdettu")
    return redirect(url_for("user_profile", user_id =  u.id))

@app.route("/users/", methods=["GET"])
@login_required_with_role(role="ADMIN")
def users_index():
    page = request.args.get('page', 1,  type=int)
    users = User.query.paginate(page, 5, False)
    next_url = url_for('users_index', page = users.next_num) \
        if users.has_next else None
    prev_url = url_for('users_index', page = users.prev_num) \
        if users.has_prev else None
    return render_template("auth/userlist.html", users = users.items,
                           next_url = next_url, prev_url = prev_url)

@app.route("/user/admin/delete/<user_id>", methods=["POST"])
@login_required_with_role(role="ADMIN")
def admin_user_delete(user_id):

    u = User.query.get(user_id)
    db.session().delete(u)
    db.session().commit()

    return redirect(url_for("users_index"))

message = None

def set_message(newMessage):
    global message 
    message = newMessage

def get_message():
    global message
    message_help = message
    message = None
    return message_help