from flask import Blueprint,session,redirect,url_for,render_template,request
from target.models import Question,Test
from target import db

admin = Blueprint("admin",__name__)

id1 = 0
def cretae_test(d=None):
    global id1
    if id1==0 and d==None:
        test = Test(description="")
        db.session.add(test)
        db.session.commit()
        id1=test.id
        return id1
    elif id1!=0:
        if d!=None:
            test = Test.query.filter_by(id=id1).first()
            test.description = d
            db.session.add(test)
            db.session.commit()
            return test.id
        return id1 
@admin.route("/createTest/<string:action>")
@admin.route("/createTest",defaults={'action': None},methods=["GET","POST"])
def route_createTest(action):
    id2 = cretae_test()
    if action=="push":
        id2 = cretae_test("description")
        return redirect(url_for("home.route_home"))
    if action==None and request.method=="POST":
        description = request.form.get("question")
        optionA = request.form.get("optionA")
        optionB = request.form.get("optionB")
        optionC = request.form.get("optionC")
        optionD = request.form.get("optionD")
        answer = request.form.get("answer")
        question = Question(description=description,optionA=optionA,optionB=optionB,optionC=optionC,optionD=optionD,answer=answer,testId=id2)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for("admin.route_createTest"))
    return render_template("createTest.html")
