from flask import Flask, render_template,Blueprint

home = Blueprint('home',__name__)
login = Blueprint('login',__name__)


@home.route('/home')
def homepage():
    return render_template("home.html")

@login.route('/')
def loginpage():
    
    return render_template("login.html")