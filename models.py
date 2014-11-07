from app import db

class BlogPost(db.Model):

  __tablename__ = "posts"

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String, nullable=False)
  desc = db.Column(db.String, nullable=False)

  def __init__(self, title, desc):
    self.title = title
    self.desc = desc

  def __repr__(self):
    return '<Post {}>'.format(self.title)
  
