from flask import Flask, render_template, redirect, url_for, request, session, flash
import datetime, os
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
# config
# e.g.: APP_CONFIG=config.DevelopmentConfig 
app.config.from_object(os.environ['APP_CONFIG'])

# create sqlalchemy db object
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter


def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      flash('You need to login first')
      return redirect(url_for('users.login'))

  return wrap


@app.route('/')
@login_required
def home():
  current_time=datetime.datetime.now()
  #posts = models.BlogPost.query.all()
  posts = db.session.query(BlogPost).all()
  return render_template('index.html', 
    title="Home", 
    current_time = current_time,
    posts = posts
  )


@app.route('/welcome')
def welcome():
  return render_template('welcome.html')

@app.route("/about")
def about():
    return render_template('index.html', title="About")

@app.route("/contact")
def contact():
    return render_template('index.html', title="Contact Us")


if __name__ == '__main__':
  app.run()
