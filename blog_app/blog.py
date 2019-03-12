from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/kontakt/")
def contact():
    return render_template('contact.html')




