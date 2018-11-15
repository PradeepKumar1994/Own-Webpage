# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:11:30 2018

@author: Mine
"""

from app import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    
    username = db.Column(db.String(64), index = True, unique = True)
    
    email = db.Column(db.String(124), index = True, unique = True)
    
    password_hash = db.Column(db.String(124))
    

    def __repr__(self):
        
        return("<User: {}>" .format(self.username)) 