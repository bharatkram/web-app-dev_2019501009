from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    pub_year = db.Column(db.Integer, nullable=False)
    revs = db.Column(db.String, nullable=True)

class revi(db.Model):
    __tablename__ = 'revi'
    id = db.Column(db.Integer, primary_key = True)    
    username = db.Column(db.String)
    isbn = db.Column(db.String)
    rating = db.Column(db.Integer)
    review = db.Column(db.String)
