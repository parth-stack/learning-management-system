from flask import Blueprint,flash,session,redirect,url_for

dash = Blueprint("dash",__name__)

@dash.route("/logout")
def route_logout():
    if "user" in session:
        session.pop("user")
        flash("Logged out ", "success")
    else:
        flash("not in session ", "danger")
    return redirect(url_for("home.route_home"))

@dash.route("/dashboard")
def route_dashboard():
    if "user" in session:
        return "hello mother fucker"
    else:
        return redirect(url_for("dash.route_logout"))
