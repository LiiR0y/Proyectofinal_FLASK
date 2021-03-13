#Proyecto Final Grupal de FLASK
#Axel, Ramona y Loriel
from flask import Flask, render_template, url_for, request, redirect
import sqlite3 
from contextodb import *

app = Flask(__name__)


#Routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        print(request.form)
        return redirect("profile.html")
    else:
        return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/profile")
def profile():
    return render_template('profile.html')


@app.route('/course')
def course():
    
    con = sqlite3.connect('web.db')
    cursor = con.cursor()
    con.execute('SELECT * FROM usuario ')
    datos = cursor.fetchall()
    return render_template('course.html', usuario = datos)

if __name__ == "__main__":
    app.run(debug=True)