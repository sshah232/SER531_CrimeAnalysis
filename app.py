from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
import MLFunctions as ml
import graph
from flask_session import Session
import io
from flask import Response
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
import numpy as np
import pandas as pd
import json
import plotly
import plotly.express as px
from SparQL import run_sparql_query2
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user, current_user

from io import BytesIO
import random



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///CrimeAnalysis.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

con = sqlite3.connect("instance/CrimeAnalysis.db")
cur = con.cursor()

class CrimeAnalysis(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


@app.route('/chart')
def bar_with_plotly():
    df_sparql = run_sparql_query2()

    # Print the DataFrame to understand its structure
    print(df_sparql)

    # Plot the DataFrame using Plotly
    fig = px.bar(df_sparql, x='Gender', y='Description', title='Crime Count by Gender and Description')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphJSON=graphJSON)
 
# @app.route('/chart')
# def show_sparql_results():
#     # Call the function to get results
#     sparql_results = run_sparql_query1()
#     print(sparql_results)
#     # Pass the results to the template or use as needed
#     return render_template('dashboard.html', sparql_results=sparql_results)

@app.route('/chart')
def index():
    # Run your SPARQL query and get the DataFrame
    df = run_sparql_query2()

    # Convert DataFrame to HTML
    html_table = df.to_html(classes='table table-striped table-bordered')
    print("Test")
    # Pass the HTML table to the template
    return render_template('dashboard.html', html_table=html_table)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if current_user.is_authenticated:
        msg = 'Welcome back, ' + current_user.username
    else:
        msg = ''
    return render_template('homepage.html', msg=msg)

@app.route('/login', methods=['POST'])
def login_fn():
    if request.method == 'POST':
        username = request.form['LoginForm-name']
        password = request.form['LoginForm-pass']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/")
        else:
            flash('Login failed. Check your username and password.')

    return redirect("/")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

if __name__ == "__main__":
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # show_sparql_results()
    app.run(debug=True, port=8000)