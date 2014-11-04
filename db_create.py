from app import db
from models import BlogPost

#create db
db.create_all()

#insert 
db.session.add(BlogPost("title", "description"))
db.session.add(BlogPost("Good", "I'm good"))
db.session.add(BlogPost("Well", "I'm well"))

#commit the changes
db.session.commit()
