# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 08:27:05 2018

@author: Mine
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLALCHEMY
from flask_migrate import Migrate

app = Flask(__name__, static_url_path = '/static')
app.config.from_object(Config)
db = SQLALCHEMY(app)    #represents the database
migrate = Migrate(app, db)  #represents migration engine

from app import routes, models

app.config['TEMPLATES_AUTO_RELOAD'] = True