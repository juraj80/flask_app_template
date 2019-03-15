from flask import Flask, render_template
from random import choice

from data import jokes

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/kontakt/")
def contact():
    return render_template('contact.html')

@app.route("/vtip/")
@app.route("/vtip/<name>/")
def joke(name="Tajomný neznámy"):
    return render_template('joke.html', joke=choice(jokes), name=name)





