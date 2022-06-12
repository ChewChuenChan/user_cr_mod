from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/read')

@app.route('/read')
def read_all():
    user_list = User.get_all()
    return render_template("read.html",user_list = user_list)

@app.route('/new')
def new_user():
    return render_template ("create.html")

@app.route('/create',methods=["POST"])
def create():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')