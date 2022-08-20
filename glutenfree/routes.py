from flask import render_template
from glutenfree import app, db
from glutenfree.models import Category, Recipe


@app.route("/")
def home():
    return render_template("base.html")