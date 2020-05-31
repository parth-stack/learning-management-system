from flask import Blueprint,render_template

home = Blueprint("home",__name__)

@home.route("/")
@home.route("/home")
def route_home():
    return render_template("home.html",title="Home")

@home.route("/about")
def route_about():
    return render_template("about.html",title="about")