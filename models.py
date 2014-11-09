from app import db, bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BlogPost(db.Model):

  __tablename__ = "posts"

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String, nullable=False)
  desc = db.Column(db.String, nullable=False)
  author_id = db.Column(db.Integer, ForeignKey('users.id'))

  def __init__(self, title, desc):
    self.title = title
    self.desc = desc

  def __repr__(self):
    return '<Post {}>'.format(self.title)
  
class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False)
  passwd = db.Column(db.String, nullable=False)
  posts = relationship("BlogPost", backref="author")

  def __init__(self, name, email, passwd):
    self.name = name
    self.email = email
    self.passwd = bcrypt.generate_password_hash(passwd)

  def __str__(self):
    return '<User {}'.format(self.name)
