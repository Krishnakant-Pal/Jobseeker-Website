from flask import Flask, render_template,Blueprint

signup = Blueprint('signup',__name__)


@signup.route('/signup')
def signupboth():
    return render_template("signup.html")


