from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import string
import os

app = Flask(__name__)


def write_in_url_file(longurl,shorturl):
    urlfile = open("urlFile.text",'w')
    stored_url = str(longurl)+":"+str(shorturl)+"\n"
    urlfile.write(str(stored_url))
    urlfile.close() 

def check_if_string_in_file(file_name, string_to_search):
  
   
    with open(file_name, 'r') as read_obj:
        
        for line in read_obj:
      
            if string_to_search in line:
                return True
    return False

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters,k=3)
        rand_letters = "".join(rand_letters)
        shorten_url = check_if_string_in_file("urlFile.text",str(rand_letters))
        if not shorten_url:
            return rand_letters

 
@app.route('/',methods=['POST','GET'] )
def home():
    if request.method == 'POST':
        url_recevied = request.form["nm"]
        found_url = check_if_string_in_file("urlFile.text",str(url_recevied))
        if found_url:
            return "short url"
        else:
            short_url = shorten_url()
            write_in_url_file( url_recevied,short_url) 
        return short_url
    else:
        return render_template("url_page.html")

@app.route('/assignment')
def hello_assign():
    return "Assignment"

if __name__ == '__main__':
    app.run(port=5000,debug=True)
