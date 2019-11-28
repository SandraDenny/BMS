#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:01:11 2019

@author: admaren
"""

manage_accounts_contents="""
1.add a new account
2.account closing
3.list of users
4.edit user details
:"""
def manage_account_viewfunc():
    
    mres = input(manage_accounts_contents)
    if mres == "1":
        add_new_account_func()
    elif mres == "2":
        closing_account_func()
    elif mres == "3":
        list_of_users_func()
    


def add_new_account_func():
    print(" wer are going to add new account")
    uname  = input("Please enter your name:")
    
    print(f"Entered name is {uname}")
    uadress =input("please enter your adress:")
    print(f"entered adress is {uadress}")
    uinitialdeposit = input("please enter your initial amount of deposit (not less than 500):")
    print(f"entered initial amount of deposit is {uinitialdeposit}")
    uaccounttypefunc()
    
uaccounttypecontents="""
Choose your account type

1.savings account
2.current account
"""

def uaccounttypefunc():
    res=input(uaccounttypecontents)
    if res=="1":
        create_saving_acc_func()
    elif res=="2":
        create_current_acc_func()
        
    
def create_saving_acc_func():
    print("savings account created")
def create_current_acc_func():
    print("current account created")
    print("your account number is:")   
    
def closing_account_func():
    print("we are going to delete an exixting account")
    uaccountno = input("please enter your account number:")
    print(f"account number {uaccountno} is deleted")

def list_of_users_func():
    print(f"the list of account holders are:")
    

    
    
    
    
    
        
        
    


        
    