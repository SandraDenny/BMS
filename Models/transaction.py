#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:27:14 2019

@author: admaren
"""

from .dbmodels import TransactionModel

class Transaction:
    def __init__(self):
        print("exixting account functions")
        self.amount =0
        

        

    
    def addTransactionToDB(self, accmodel):
        """Function used to add transation to the user
        
        amount : transaction amount
        """
        trmodel = TransactionModel.create(amount=self.amount, account= accmodel)
        return trmodel
    
    def showTransactions(self):
        pass
     
            
        