#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:03:46 2019

@author: admaren
"""

class User:
    
    def __init__(self):
        print("New user creation")
        self.Name = None
        self.Address = None
        self.DOB = None
        self.iDeposit = 0.0
        self.acc_valid = False
        self.transactions = []
    
    def putInitialDeposit(self, amount):
        if amount < 500:
            print("Initial deposit must not be less than 500 INR")
            self.acc_valid = False
        else:
            self.acc_valid = True
            
        self.addTransaction(amount)
        
    
    
    def addTransaction(self, amount):
        pass
    
    def showTransactions(self):
        pass
            
        
    

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