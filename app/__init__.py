# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 08:27:05 2018

@author: Mine
"""

from flask import Flask

from config import Config

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

app = Flask(__name__) #, static_url_path = '/static' add later if nothing works out for db init

app.config.from_object(Config)

db = SQLAlchemy(app)    #represents the database instance

migrate = Migrate(app, db)  #represents migration engine instance

from app import routes, models

app.config['TEMPLATES_AUTO_RELOAD'] = True