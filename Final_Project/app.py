from datetime import datetime
import sqlite3
from flask import Flask, flash, redirect, render_template, session, request
from werkzeug.security import check_password_hash, generate_password_hash
import logging 
import string as str_module

from helper import login_required

app = Flask(__name__)
app.logger.setLevel(logging.INFO) 
app.config["SECRET_KEY"] = "Final_Project" 

connect = sqlite3.connect("new_database.db")

@app.route("/", methods=["GET", "POST"])
@login_required
def home():

    if request.method == "POST":
        note = request.form.get("note").strip()
        if not note:
            flash("Please type in a note", category="error")
        else:
            user_id = session["user_id"]
            current_time = datetime.now()
            db.execute("INSERT INTO note (user_id, data, date) VALUES (?, ?, ?)", session["user_id"], note, current_time)

    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            flash("Username Needed", category="error")
            return redirect("/")
        password = request.form.get("password")
        if not password:
            flash("Password Needed", category="error")
            return redirect("/")

        user = db.execute("SELECT * FROM user WHERE username = ?", request.form.get("username")
                    )
        if len(user) != 1 or not check_password_hash(
            user[0]["password_hash"], request.form.get("password")
        ):
            flash("username or password incorrect", category="error")
            return redirect("/")

        session["user_id"] = user[0]["id"]

        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/logout")
@login_required
def logout():

    session.clear()

    return redirect("/")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

        if request.method == "POST":

            username = request.form.get("username")
            if not username:
                flash("must provide username", category="error")
                return redirect("/sign-up")

            password = request.form.get("password")
            confirmation = request.form.get("confirmation")
            if not password or not confirmation or password != confirmation or not password_meets_requirments(password):
                flash("must provide password and confirmation, must match, must meet requirments", category="error")
                return redirect("/sign-up")

            user = db.execute("SELECT * FROM user WHERE username = ?", request.form.get("username"))

            if len(user) != 0:
                flash("username already exists", category="error")
                return redirect("/sign-up")

            db.execute("INSERT INTO user (username, password_hash) VALUES(?, ?)",
                       request.form.get("username"), generate_password_hash(request.form.get("password")))

            user_id = db.execute("SELECT LAST_INSERT_ROWID() AS id")

            session["user_id"] = user_id[0]["id"]

            return redirect("/")
        else:
            return render_template("sign_up.html")

@app.route("/Notes", methods=["GET", "POST"])
@login_required
def Notes():

    notes = db.execute(
        "SELECT id, data, date FROM note WHERE user_id = ? ORDER BY date DESC", session["user_id"]
        )
    return render_template("notes.html", notes=notes)

@app.route("/delete-note", methods=["POST"])
def delete_note():

    if request.method == "POST":
        note_id = request.form.get("note_id")
        app.logger.info("Note ID to delete: %s", note_id) # this is from cs50.ai
        if note_id:
            db.execute("DELETE FROM note WHERE id = ?", note_id)
            flash("Delete Successful", category="success")
    return redirect("/Notes")

## I reused this code from finance problem set it was my code and figured it would be easier then rewriting it or comming up with a new one.
@app.route("/password_meets_requirments", methods=["GET", "POST"])
def password_meets_requirments(password):

    if len(password) < 8:
        return False

    has_alpha = False
    has_digit = False
    has_punct = False

    for char in password:
        if char.isalpha():
            has_alpha = True
        elif char.isdigit():
            has_digit = True
        elif char in str_module.punctuation:
            has_punct = True
    if has_alpha and has_digit and has_punct:
        return True
    else:
        return False