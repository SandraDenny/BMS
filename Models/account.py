#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:27:14 2019

@author: admaren
"""

class account:
    def __init__(self):
        print("exixting account functions")
        self.transactions = []
        
    def putInitialDeposit(self, amount):
        if amount < 500:
            print("Initial deposit must not be less than 500 INR")
            self.acc_valid = False
        else:
            self.acc_valid = True
            
        self.addTransaction(amount)
        

    
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
            
        