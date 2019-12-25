#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:27:14 2019

@author: admaren
"""
_hdr  = "\n"*2 +36*"#"+"\n"*2 
from .dbmodels import AccountModel, TransactionModel
from .transaction import Transaction

class Account:


    @staticmethod
    def AccountAddToDB(user, atype):
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
        
        return bal
        
        #print(f"Account balance :{bal}")
    
    @staticmethod
    def deposit(acc_id:int, amount:float):
        """function used to deposit money : deposit amount
        """
        t0 = Transaction()
    
        t0.amount = (float(amount))
        aq = AccountModel.select().where(AccountModel.id == acc_id)
        
        # add transaction to transaction db with selected account id
       # print(_hdr)
        for acc in aq:
            t0.addTransactionToDB(acc)
       #     print(f"Transaction added to account :{acc_id}, amount :{amount}")
      #  print(_hdr)
        
        
        

    
    

       
    @staticmethod
    def showTransactions(accountno):
        """function used to see the transactions undertaken in the account : transactions with their transaction id
        """
        query = TransactionModel.select().join(AccountModel).where(AccountModel.id == int(accountno))
    
        # print(_hdr)
        # print(f"Transaction details for the account {accountno} are ")
        reslist = []
        for tr in query:
            amt = tr.amount
            dstr = tr.date.strftime("%d,%B %Y")
            v = f"{dstr} ...  {amt:12.3f}"
            reslist.append(v)
        return reslist
            
        