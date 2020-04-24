import csv
import os
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False

db.init_app(app)

def main():
    app.app_context().push()
    db.create_all()
    
    f = open("books.csv")
    reader = csv.reader(f)
    counter = 0
    # for isbn, title, author, pub_year in reader:
    #     if isbn == "isbn":
    #         continue
    #     counter += 1
    #     book = Book(id=counter, isbn=isbn, title=title, author=author, pub_year=int(pub_year))
    #     db.session.add(book)
    #     print(f"{counter}) Added {title} with {isbn} written by {author} in {pub_year}.")
    rev = revi(id=1,username='sid',isbn='0380795272',rating=4,review='Amazing Book')
    db.session.add(rev)
    rev = revi(id=2,username='sudheer',isbn='0380795272',rating=4,review='Amazing Book')
    db.session.add(rev)
    db.session.commit()
    print('added')
if __name__ == "__main__":
    main()