from flask import Flask, render_template, request,
import random
import string
import os

app = Flask(__name__)


def write_in_url_file(longurl,shorturl):
    urlfile = open("urlFile.text",'a')
    stored_url = str(longurl)+":"+str(shorturl)+"\n"
    urlfile.write(str(stored_url))
    urlfile.close() 


def check_if_string_in_file(file_name, string_to_search): 
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                shorturl = line.replace(string_to_search+":","")
                return str(shorturl)
    return False

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters,k=3)
        rand_letters = "".join(rand_letters)
        shorten_url = check_if_string_in_file("urlFile.text",str(rand_letters))
        if not shorten_url:
            return rand_letters+".io"

 
@app.route('/',methods=['POST','GET'] )
def home():
    if request.method == 'POST':
        url_recevied = request.form["nm"]
        found_url = check_if_string_in_file("urlFile.text",str(url_recevied))
        if found_url:
            return found_url
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
