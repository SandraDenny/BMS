#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:30:50 2019

@author: admaren
"""

import datetime
from peewee import *

db = SqliteDatabase('bms_test.db')

class BaseModel(Model):
    class Meta:
        database = db

class UserModel(BaseModel):
    Name = CharField(unique=False)
    Address = CharField(unique=False)
    DOB = DateTimeField()




class AccountModel(BaseModel):
    accounttype = CharField()
    user = ForeignKeyField(UserModel, backref='accounts')
    
class TransactionModel(BaseModel):
    amount = FloatField()
    account = ForeignKeyField(AccountModel, backref='transactions')
    


if __name__ == "__main__":
#    db.create_tables([UserModel, AccountModel, TransactionModel])
#    
#    
#    
#    
#    user2 = UserModel.create(Name = "User2", Address = "pilakkat house", DOB = datetime.datetime.now())
#    
#    acc = AccountModel.create(user= user2, accounttype="CURRENT")
#    
#    for i in range(10):
#        TransactionModel.create(amount = i *10, account= acc)
#
##
    
    transquery = TransactionModel.select().join(AccountModel).where(AccountModel.accounttype=="SAVINGS")
    for t in transquery:
        print(t.account.user.Name)
