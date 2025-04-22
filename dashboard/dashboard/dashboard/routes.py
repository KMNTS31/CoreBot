from flask import render_template
from dashboard.dashboard.dashboard.app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
