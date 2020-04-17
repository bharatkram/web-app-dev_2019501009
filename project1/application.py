import os

from flask import Flask, session, render_template, request, url_for, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import datetime

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


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", act = 0)
    elif request.form.get("but") == "Login":
        name = request.form.get("usr")
        user = db.execute("SELECT * FROM users WHERE username = :name", {"name": name}).fetchone()
        print(user)
        if user is not None:
            psw = request.form.get("psw")
            if user[1] == psw:
                session["username"] = user[0]
                return redirect(url_for('userhome'))
        return render_template("register.html", act = 0.1)
    else:
        name = request.form.get("usr")
        user = db.execute("SELECT username FROM users WHERE username = :name", {"name": name}).fetchone()
        print(user)
        if user is None:
            psw = request.form.get("psw")
            db.execute("INSERT INTO users (username, password, time) VALUES (:name, :psw, :time)", {"name":name, "psw":psw, "time":datetime.datetime.now()})
            print(f"Added user with username: {name}.")
            db.commit()
            return render_template("register.html", act = 1)
        else:
            return render_template("register.html", act = -1)


@app.route("/admin")
def admin():
    users = db.execute("SELECT * FROM users").fetchall()
    return render_template("admin.html", users = users)


@app.route("/userhome")
def userhome():
    if session.get("username") is not None:
        return render_template("userhome.html", act = 1)
    return redirect(url_for('register'))


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))
