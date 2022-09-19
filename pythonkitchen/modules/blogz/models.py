
from init import db
from sqlalchemy.ext.hybrid import hybrid_property
from shopyo.api.models import PkModel
from modules.box__default.auth.models import User

post_user = db.Table('post_user',
                    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
                    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
                    )


# db.Model
class Blog(PkModel): 
    __tablename__ = "posts"   

    title = db.Column(db.String)
    source = db.Column(db.Text) # markdown

    slug = db.Column(db.String(200))
    featured_image = db.Column(db.String) # link
    authors = db.relationship('User', secondary=post_user, backref='posts')
    pub = db.Column(db.DateTime)
