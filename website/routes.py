from flask import Flask, render_template,Blueprint

home = Blueprint('home',__name__)


@home.route('/')
def homepage():
    return render_template("home.html")