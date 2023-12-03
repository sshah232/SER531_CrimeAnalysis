from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
import dbfunctions
import MLFunctions
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

from io import BytesIO
import random



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

con = sqlite3.connect("instance/todo.db")
cur = con.cursor()

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

class Cart(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(500), nullable=True)
    name = db.Column(db.String(200), nullable=True)
    price= db.Column(db.Integer, nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    total = db.Column(db.Integer, nullable=True)

    def __repr__(self) -> str:
            return f"{self.sno} - {self.name}"

class products(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    prod_img = db.Column(db.String(200), nullable=False)
    prod_name = db.Column(db.String(500), nullable=False)
    prod_price = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
            return f"{self.sno} - {self.prd_name}"



@app.route('/chart')
def bar_with_plotly():
    low10=MLFunctions.getlowdata()
    top10=MLFunctions.getdata()
    fig = px.bar(top10, x=top10.index, y=top10.values,  barmode='group')
    fig2 = px.bar(low10, x=low10.index, y=low10.values,  barmode='group')
    # Create graphJSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    #freq1=MLFunctions.frequentproducts()
    # assoc1=MLFunctions.getassoc_rules()
    #freq=list(freq1.itemsets)
    # assoc=set(assoc1.consequents)
    #print(freq)
    # print(assoc)
    return render_template('dashboard.html', graphJSON=graphJSON,graphJSON2=graphJSON2,top10=top10,low10=low10#freq=freq,assoc=assoc
                           )
 

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        image = request.form['img']
        name = request.form['name']
        price = request.form['price']
        quantity= 1
        total= price*quantity
        todo = Cart(image=image,name=name,price=price,quantity=quantity,total=total)
        db.session.add(todo)
        db.session.commit()
        
    if not session.get("name"):
        msg='You are not logged in'
    else:
         msg='Welcome back, '+ session.get("name")
    #prdinfo=dbfunctions.getprd_info()
    #prdinfo=products.query.all()
    prdinfo=dbfunctions.getprd_info()
    tcount=dbfunctions.getCount()
    totalcart=dbfunctions.getTotal()
    allCart = Cart.query.all()
    return render_template('homepage.html',prdinfo=prdinfo,msg=msg,tcount=tcount, allCart=allCart,totalcart=totalcart)



@app.route('/products', methods=['GET', 'POST'])
def hello_world3():
    if request.method=='POST':
        image = request.form['img']
        name = request.form['name']
        price = request.form['price']
        quantity= 1
        total= price*quantity
        todo = Cart(image=image,name=name,price=price,quantity=quantity,total=total)
        db.session.add(todo)
        db.session.commit()
    allproducts=moreproducts.getproducts()
    tcount=dbfunctions.getCount()
    totalcart=dbfunctions.getTotal()
    allCart = Cart.query.all()
    return render_template('category.html', allproducts=allproducts,tcount=tcount, allCart=allCart,totalcart=totalcart)

@app.route('/login', methods=['POST'])
def login_fn():
    if request.method=='POST':
        name = request.form['LoginForm-name']
        password = request.form['LoginForm-pass']
        if(dbfunctions.validateuser(name,password)):
             session["name"] = name
        return redirect("/")
        
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)




@app.route('/add/<int:sno>',methods=['GET', 'POST'])
def add(sno):
    dbfunctions.addproduct(sno)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)