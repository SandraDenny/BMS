#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:30:50 2019

@author: admaren
"""

import datetime
from peewee import *

db = SqliteDatabase('bms.db')

class BaseModel(Model):
    class Meta:
        database = db

class UserModel(BaseModel):
    Name = CharField(unique=False)
    Address = CharField(unique=False)
    DOB = DateTimeField()
    

