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

        self.acc_valid = False
        self.transactions = []
    
    
    
    
    def balenquiry(self):
        """function used to check the balance in the account : bal amount
        """
        pass
    def deposit(self):
        """function used to deposit money : deposit amount
        """
        pass
    def withdrawal(self):
        """function used to withdraw money : withdrawal amount
        """
        pass
    def showtransaction(self):
        """function used to see the transactions undertaken in the account : transactions with their transaction id
        """
        pass
    def edituserdetails(self):
        """function used to edit the users information : modifications
        """
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