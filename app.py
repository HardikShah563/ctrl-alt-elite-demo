from flask import Flask, url_for, request, redirect, flash
from flask.templating import render_template
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import psycopg2.extras
from test import *

app = Flask(__name__)

# ---------------------------------------------

details = []
osDetails = []
allFiles = []

@app.route('/')
def home(): 
    osDetails = os_details()
    allFiles = all_files()
    return render_template('home.html',len1 = len(osDetails), osDetails = osDetails, allFiles = allFiles, len2 = len(allFiles))

@app.route('/login')
def login(): 
    return render_template('login.html')

@app.route('/register')
def register(): 
    return render_template('register.html')

def scan(): 
    # osDetails = os_details()
    return render_template('home.html', osDetails = osDetails)
    print("Hello world")

if __name__ == '__main__': 
    app.run(debug = True)
    # app.run(debug = False, host = '0.0.0.0')

# 0.0.0.0 will ensure that my website is visible publically