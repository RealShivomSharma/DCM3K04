#Contains login screen and authentication

from flask import Blueprint 
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/register')
def register():
    return "<p>register<p>"