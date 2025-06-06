from flask import Blueprint, render_template

viewss = Blueprint('views', __name__)

@viewss.route('/')
def home():
    return render_template("home.html")


@viewss.route('/second')
def second():
    return render_template("second.html")

@viewss.route('/third')
def third():
    return render_template("third.html")

@viewss.route('/Google_form')
def Google_form():
    return render_template("Google_form.html")
@viewss.route('/Success')
def Success():
    return render_template("Success.html")
@viewss.route('/spanishVersion')
def spanishVersion():
    return render_template("spanishVersion.html")
@viewss.route('/SpanishGoogleForm')
def SpanishGoogleForm():
    return render_template("SpanishGoogleForm.html")
@viewss.route('/SpanishSuccess')
def SpanishSuccess():
    return render_template("SpanishSuccess.html")

@viewss.route('/Map')
def Map():
    return render_template("Map.html")

