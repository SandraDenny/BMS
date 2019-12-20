#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:03:46 2019

@author: admaren
"""

from .dbmodels import UserModel,AccountModel
import datetime
class User:
    
    def __init__(self):
        print("New user creation")
        self.Name = None
        self.Address = None
        self.DOB = None

        self.acc_valid = False
        self.transactions = []
    
    
    def AddToDB(self):
        u = UserModel.create(Name = self.Name, Address = self.Address, DOB = datetime.datetime.now())
        return u
    
    @staticmethod
    def ListUsers():
        q = UserModel.select()
        
        
        for v in q:
            aq = AccountModel.select().join(UserModel).where(UserModel.id==v.id).execute()
            print(f"Username :{v.Name}   AccountNumber:{aq[0].id}")
        input("Press any key to continue...")
        
    @staticmethod
    def Balance():
        q = UserModel.select().where(UserModel.id == 0)
            
if __name__ == "__main__":
    import sys
    sys.path.append("/home/admaren/Documents/BankManagementSys")
    User.ListUsers()

            
        
    

#
#
#sandra = User()
#sandra.Name = "Sandra"
#
#
#user2 = User()
#user2.Name = "Rahul"
#
#user2.Address = "sfsljdlkfjslf"
#
#
#print(sandra.Name)