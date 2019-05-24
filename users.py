from flask import Blueprint, render_template, request

users = Blueprint('users',__name__)

@users.route('/')
def index():
    return render_template("template.html",
                            title='Welcome to our page',
                            greeting='Welcome Hoooman', 
                            message='We are glad you came')

@users.route("/users/home", methods=['POST'])
def userHome():
    return render_template("template.html",
                            title='Users section',
                            greeting='Hello {}'.format(request.form['username']), 
                            message='How are you, {}'.format(request.form['username']))