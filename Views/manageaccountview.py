#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:01:11 2019

@author: admaren

"""

import sys

sys.path.append("/home/admaren/Documents/BankManagementSys")

_hdr  = "\n"*2 +36*"#"+"\n"*2 

from Models import User, Account, Transaction

manage_accounts_contents="""

USER MANAGEMENT
==== =========

1.add a new account
2.account closing
3.list of users

Enter x to exit this page
:"""
def manage_account_viewfunc():
    
    while 1:
    
        mres = input(manage_accounts_contents)
        if mres == "1":
            add_new_account_func()
        elif mres == "2":
            closing_account_func()
        elif mres == "3":
            list_of_users_func()
            
        elif mres == "x":
            break
    


def add_new_account_func():
    print(" wer are going to add new account")
    newuser = User()
    uname  = input("Please enter your name:")
    newuser.Name = uname
    print(f"Entered name is {uname}")
    
    uadress =input("please enter your adress:")
    newuser.Address = uadress
    print(f"entered adress is {uadress}")
    
    DOB = input("please enter your DOB:") # string 
    newuser.DOB = DOB # convert DOB to datetime datatime
    print(f"entered DOB is {DOB}")
    
    umodel = newuser.AddToDB()
    

    
    typ = uaccounttypefunc()
    amodel = Account.AccountAddToDB(umodel, typ)
    
    uinitialdeposit = input("please enter your initial amount of deposit (not less than 500):")
    print(f"entered initial amount of deposit is {uinitialdeposit}")
    
    t0 = Transaction()
    
    t0.amount = float(uinitialdeposit)
    t0.addTransactionToDB(amodel)
#    newuser.putInitialDeposit(float(uinitialdeposit))
    
    
    
    
uaccounttypecontents="""
Choose your account type

1.savings account
2.current account
"""

def uaccounttypefunc():
    res=input(uaccounttypecontents)
    if res=="1":
        return "SAVINGS"
    elif res=="2":
        return "CURRENT"
        

    
def closing_account_func():
    print("we are going to delete an exixting account")
    uaccountno = input("please enter your account number:")
    print(f"account number {uaccountno} is deleted")

def list_of_users_func():
    print(_hdr)
    print(f"the list of account holders are:")
    User.ListUsers()
    
    print(_hdr)

    
    
    
    
    
        
        
    


        
    