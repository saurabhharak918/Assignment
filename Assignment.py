from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import string
import os

app = Flask(__name__)

 
@app.route('/',methods=['POST','GET'] )
def home():
    if request.method == 'POST':
        url_recevied = request.form["nm"]
        return url_recevied
    else:
        return render_template("home.html")

@app.route('/assignment')
def hello_assign():
    return "Assignment"

if __name__ == '__main__':
    app.run(port=5000,debug=True)
