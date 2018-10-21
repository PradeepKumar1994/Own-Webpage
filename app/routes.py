# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import render_template, redirect, flash, make_response, request
from app import app
from tinydb import TinyDB, Query
import pandas as pd
from app.forms import LoginForm

tiny_db = TinyDB('contact.json')
#tiny_db.insert({'first': 'No one', 'last': 'No one', 'email': 'No one'})
Querying_ = Query()
#result = tiny_db.search(Querying_.first == 'No one')


#, static_url_path = '/static'
#app = Flask(__name__, static_url_path = '/static')


@app.route('/')
@app.route('/Home')
def homepage():
    
    return render_template('Homepage.html')


@app.route('/index')
def index():
    
    user = {'username':'Pradeep'}
    
    return render_template('index.html', user = user)
    
    

@app.route('/login', methods = ['GET','POST'])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        
        flash("Hello user: {} ; remember me {}" .format(
                form.username.data, form.remember_me.data))
        
        return redirect('/index')#change to /index when you deal with the url
    
    else:
        
        return render_template('login.html', form = form, title = "Sign In")


@app.route('/ProjectP/<name>', methods = ['GET','POST'])
def hello(name):
    #name = 'Pradeep Kumar Paladugula'
    #name = 'No one'

    headings = ['TITLE']

    #CRN = [1265,12668,21862]
    
    a = pd.read_csv('E:\Python34\Task2\website\Courses.csv', header = None)
    
    del a[1]
    
    TITLE = list(a[0])

    #TITLE = ['WEB PROGRAMMING I','ADVANCE DATABASE SYSTEM DESIGN','PROBABISLISTIC DATA MANAGEMENT']
    
    #template_location = 'Hello.html'

    if(name == 'resume'):
 
        return render_template('hello.html', name=name, headings = headings, TITLE = TITLE)

    elif(name == 'Arya Stark'):

        return render_template('hello.html', name=name)

    if(name == 'Contact Information Page'):
        
        return render_template('Contact_Information.html')
        
        #template_location = 'Contact_Information.html'
    
    if(name == 'post_contact_info'):
        
        return contact_info_data()

    return render_template('Hello.html', name = name)


@app.route('/ProjectP/post_contact_info')
def contact_info_data():
    
    if request.method == 'POST':
    
        info = [request.form['first'],
                    request.form['last'],
                    request.form['email']]
            
        tiny_db.insert({'first': request.form['first'],
                            'last': request.form['last'],
                            'email': request.form['email'],
                            })
    
        return render_template('Contact_Information.html', info = info)


