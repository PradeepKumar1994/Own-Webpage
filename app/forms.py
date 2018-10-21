# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 17:32:46 2018

@author: Mine
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    
    username = StringField("Username", validators = [DataRequired()])
    
    password = PasswordField("Password", validators = [DataRequired()])
    
    remember_me = BooleanField("Remember Me")
    
    submit = SubmitField('Sign In')
    
    