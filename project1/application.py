import os

from flask import Flask, session,flash, render_template, request, url_for, redirect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import datetime
import random

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("username") != None:
        return redirect(url_for('userhome'))
    if request.method == "GET":
        return render_template("register.html", act=0)
    else:
        name = request.form.get("usr")
        user = db.execute("SELECT username FROM users WHERE username = :name", {
                          "name": name}).fetchone()
        print(user)
        if user is None:
            psw = request.form.get("psw")
            db.execute("INSERT INTO users (username, password, time) VALUES (:name, :psw, :time)", {
                       "name": name, "psw": psw, "time": datetime.datetime.now()})
            print(f"Added user with username: {name}.")
            db.commit()
            return render_template("register.html", act=1)
        else:
            return render_template("register.html", act=-1)


@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "GET":
        return redirect(url_for('register'))
    name = request.form.get("usr")
    user = db.execute(
        "SELECT * FROM users WHERE username = :name", {"name": name}).fetchone()
    print(user)
    if user is not None:
        psw = request.form.get("psw")
        if user[1] == psw:
            session["username"] = user[0]
            return redirect(url_for('userhome'))
    return render_template("register.html", act=0.1)


@app.route("/admin")
def admin():
    users = db.execute("SELECT * FROM users").fetchall()
    return render_template("admin.html", users=users)


@app.route("/userhome", methods=["GET", "POST"])
def userhome():
    if session.get("username") is None:
        return redirect(url_for('register'))
    if request.method == "POST":
        sel = request.form.get("sel")
        inp = request.form.get("str")

        sql = f"SELECT title, isbn, author FROM books WHERE {sel} LIKE '%{inp}%'"
        books = db.execute(sql).fetchall()
        empty = False
        if books == []:
            empty = True
        return render_template("userhome.html", books=books, empty=empty)
    return render_template("userhome.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))

@app.route("/bookpage",methods=["GET"])
@app.route("/bookpage/<isbn>", methods=["GET", "POST"])
def bookpage(isbn):
    # isbn = request.form.get("isbn")
    # print("here",isbn)
    book = db.execute(

            "SELECT title, author, pub_year FROM books WHERE isbn= :isbn", {"isbn": isbn}).fetchall()
    print(book)
    imageurl = "http://covers.openlibrary.org/b/isbn/"+isbn+"-M.jpg"
    row =db.execute("SELECT id FROM books WHERE isbn = :isbn",
                        {"isbn": isbn}).fetchall()
    # print(row)
    if request.method == "POST":
        username = session['username']
        rating = request.form.get('rating')
        review = request.form.get('comment')
        rev = db.execute("SELECT * FROM revi where username = :username and isbn= :isbn",{"username":username,"isbn":isbn})
        rev1=rev.fetchall()
        # print(rev1)
        if rev.rowcount == 1:
            rev = db.execute("SELECT * FROM revi where isbn= :isbn",{"username":username,"isbn":isbn}).fetchall()
            flash("You have already submitted review",'warning')
            print("inside if")
            print(rev)
            return redirect("/bookpage/"+isbn)
       
        rating = int(rating)    
        db.execute("Insert INTO revi(username,isbn,rating,review) VALUES \
        (:username,:isbn,:rating,:review)",
        {
            "username": username, "isbn": isbn,"rating":rating,"review":review})
        db.commit()
        flash("Review submitted")
        rev = db.execute("SELECT * FROM revi where isbn= :isbn",{"username":username,"isbn":isbn}).fetchall()
        print("if return")
        print(rev)
        return render_template("book.html", title=book[0][0], author=book[0][1], year=book[0][2],review = rev,imageurl =imageurl)
    else:
        username = session['username']
        rev = db.execute("SELECT * FROM revi where isbn= :isbn",{"username":username,"isbn":isbn}).fetchall()
        print("inside else")
        # print(book)
        # print(rev)
        # flash("SUccessful")
        return render_template("book.html", title=book[0][0], author=book[0][1], year=book[0][2],review = rev,imageurl =imageurl)

        # "SELECT title, author, pub_year FROM books WHERE isbn= :isbn", {"isbn": isbn}).fetchall()
    # imageurl = "http://covers.openlibrary.org/b/isbn/"+isbn+"-M.jpg"
    # print(imageurl)
    # return render_template("book.html", title=book[0][0], author=book[0][1], year=book[0][2], imageurl=imageurl)

