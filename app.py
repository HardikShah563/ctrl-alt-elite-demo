from flask import Flask, url_for, request, redirect, flash
from flask.templating import render_template
from werkzeug.security import generate_password_hash, check_password_hash
import nmap
import os
import psycopg2
import psycopg2.extras
from test import *

app = Flask(__name__)

# ---------------------------------------------

details = []
osDetails = []
allFiles = []

def get_vulnerabilities():
    vulnerabilities = []
    num_vulnerabilities = len(vulnerabilities)
    return vulnerabilities, num_vulnerabilities

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/login')
def login(): 
    return render_template('login.html')

@app.route('/register')
def register(): 
    return render_template('register.html')

@app.route('/scan')
def scan():
    osDetails = os_details()
    allFiles = all_files()
    networkConfig = network_config()
    vulnerabilities_list, num_vulnerabilities = get_vulnerabilities()  # add this line to get vulnerabilities

    return render_template('scan.html', len1=len(osDetails), osDetails=osDetails, allFiles=allFiles, len2=len(allFiles), networkConfig=networkConfig, vulnerabilities_list=vulnerabilities_list, num_vulnerabilities=num_vulnerabilities)  

if __name__ == '__main__': 
    app.run(debug = True)
    # app.run(debug = False, host = '0.0.0.0')

# 0.0.0.0 will ensure that my website is visible publically