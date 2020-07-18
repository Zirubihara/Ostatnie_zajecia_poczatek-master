from flask import Flask, render_template, request, make_response, redirect, url_for
from models import db, User

app = Flask(__name__)
db.create_all()

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/zapisz-sie")
def zapisz_sie():
    return render_template("zapisz_sie.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

if __name__ == '__main__':
    app.run()