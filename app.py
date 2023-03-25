from flask import Flask, render_template,request
import pymongo
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template("index.html",title="Feedback_form")

@app.route('/act',methods=['POST'])
def act():
    cluster = MongoClient("mongodb+srv://admin:admin123@cluster0.mrsga84.mongodb.net/?retryWrites=true&w=majority")
    db = cluster['Feedback']
    collection = db['users']
    # data = request.form
    # print(data)
    name = request.form.get('fname')
    print(name)
    lname = request.form.get('lname')
    print(lname)
    gender = request.form.get('g')
    email = request.form.get('eml')
    cmt = request.form.get('cmt')
    post = {"name":name,"lnmae":lname,"gender":gender,"email":email,"comments":cmt}
    collection.insert_one(post)
    return render_template("index.html")

