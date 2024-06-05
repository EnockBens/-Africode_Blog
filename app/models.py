from app import db
from datetime import datetime
from sqlalchemy.orm import relationship

from app import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model , UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(120) , unique=True , nullable=False)
    image_file = db.Column(db.String(20) , nullable=False , default = 'default.jpeg')
    password = db.Column(db.String(60) ,nullable=False)
    Posts = db.relationship("Post" , backref = 'author' , lazy=True)


    def __repr__(self):
        return f"user('{self.username}' , '{self.email}' , '{self.image_file}')"
    
   
    
class Post(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(100) , nullable=False )
    content = db.Column(db.Text ,  nullable=False)
    date_posted =db.Column(db.DateTime , nullable=False , default= 'datetime.utc' )
    user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable=False)

    def __repr__(self):
        return f"post('{self.title}' , '{self.date_posted}')"

