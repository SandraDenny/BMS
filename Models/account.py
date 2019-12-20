#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:27:14 2019

@author: admaren
"""

from .dbmodels import AccountModel, TransactionModel
from .transaction import Transaction

class Account:
    def __init__(self):
#        print("exixting account functions")
        self.transactions = []
        
    def putInitialDeposit(self, amount):
        if amount < 500:
            print("Initial deposit must not be less than 500 INR")
            self.acc_valid = False
        else:
            self.acc_valid = True
            
        self.addTransaction(amount)
    
    def AccountAddToDB(self, user, atype):
        acc = AccountModel.create(user= user, accounttype=atype)
        return acc
    
    @staticmethod
    def balenquiry(accid):
        """function used to check the balance in the account : bal amount
        """
        # aq = AccountModel.select(AccountModel).where(AccountModel.id==accid).execute()[0]
        
        rq = TransactionModel.select().join(AccountModel).where(AccountModel.id==accid)
        
        bal = 0
        for tr in rq:
            bal += tr.amount
            
        
        print(f"Account balance :{bal}")
    
    @staticmethod
    def deposit(acc_id:int, amount:float):
        """function used to deposit money : deposit amount
        """
        t0 = Transaction()
    
        t0.amount = float(amount)
        aq = AccountModel.select().where(AccountModel.id == acc_id)
        
        # add transaction to transaction db with selected account id
        for acc in aq:
            t0.addTransactionToDB(acc)
            print(f"Transaction added to account :{acc_id}, amount :{amount}")
        
        
        
        
    def withdrawal(self):
        """function used to withdraw money : withdrawal amount
        """
        pass
    def showtransaction(self):
        """function used to see the transactions undertaken in the account : transactions with their transaction id
        """
        pass
            
        