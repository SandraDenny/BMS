#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:51:02 2019

@author: admaren
"""

user_home_contents = """
1.balance enquiry
2.deposit
3.withdrawal
4.show transactions
5.edit user details 
"""

user_wrong_password_result = "User Not found"
def user_home_contents_viewfunc():
    
    res1 = input(user_home_contents)
    if res1 == "1":
        balance_enquiry_func()
    elif res1 == "2":
        deposit_func()
    elif res1 == "3":
        withdrawal_func()
    elif res1 == "4":
        show_transactions_func()
    elif res1 == "5":
        edit_user_details_func()
    
def balance_enquiry_func():
    accountno = input("enter your account number :")
    print("your balace amount is")

def deposit_func():
    daccountno = input("enter your account number :")
    amount = input("enter amount of deposit :")
    print(f"you have deposited {amount}")

def withdrawal_func():
    accountno = input("enter your account number :")
    wamount = input("enter amount of withdrawal :")
    print(f"you have withdrawed {wamount}")

def show_transactions_func():
    accountno = input("enter your account number :")
    print("your transactions are:")

def edit_user_details_func():
    accountno = input("enter your account number:")
    print("your account has been edited ")
    
    
    
    
    
    