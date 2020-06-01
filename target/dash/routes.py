from flask import Blueprint,flash,session,redirect,url_for,render_template,request
from target.models import Test

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
        page = request.args.get('page', 1, type=int)
        tests = Test.query.order_by(Test.date_posted.desc()).paginate(page=page, per_page=5)
        return render_template("dashboard.html",posts=tests)
    else:
        return redirect(url_for("dash.route_logout"))
