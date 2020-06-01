from flask import Blueprint,render_template,session,redirect,url_for,request,flash
from target import db,bcrypt
from target.models import User
from target.users.forms import RegisterForm,LoginForm

users = Blueprint("users",__name__)

@users.route("/login",methods=["GET","POST"])
def route_login():
    if "user" in session:
        return redirect(url_for("home.route_home"))
    else:
        form=LoginForm()
        if request.method == "POST" and form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if(user) and bcrypt.check_password_hash(user.password,form.password.data):
                session['user']={'username':user.username,'email':user.email}
                flash('Logged in ',category='success')
                return redirect(url_for("home.route_home"))
            else:
                flash('Login Error',category='danger')
        return render_template("login.html",title="Login",form=form)

@users.route("/register",methods=["GET","POST"])
def route_register():
    if "user" in session:
        return redirect(url_for("home.route_home"))
    else:
        form=RegisterForm()
        if request.method == "POST" and form.validate():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data,password=hashed_password,email=form.email.data)
            db.session.add(user)
            db.session.commit()
            session['user']={'username':user.username,'email':user.email}
            flash('Registerd as '+form.username.data,category='success')
            return redirect(url_for("home.route_home"))
        return render_template("register.html",title="Register",form=form)

