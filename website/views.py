from flask import Blueprint, render_template

viewss = Blueprint('views', __name__)

@viewss.route('/')
def home():
    return render_template("home.html")


@viewss.route('/second')
def second():
    return render_template("second.html")

