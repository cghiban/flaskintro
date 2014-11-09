from flask import flash, render_template, redirect, url_for, request, session, Blueprint
from app import app
from flask.ext.bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from functools import wraps

users_blueprint = Blueprint('users', __name__,
      template_folder = 'templates'
)

def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      flash('You need to login first')
      return redirect(url_for('login'))

  return wrap

@users_blueprint.route('/login', methods = ['POST', 'GET'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['u'] != 'admin' or request.form['p'] != 'admin':
      error = 'Invalid credentials. Try again'
    else:
      session['logged_in'] = True
      flash("Just logged in")
      return redirect(url_for('home'))
  return render_template('login.html', error = error)

@users_blueprint.route('/logout')
@login_required
def logout():
  session.pop('logged_in', None)
  flash("Just logged out")
  return redirect(url_for('welcome'))

