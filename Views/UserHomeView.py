#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:51:02 2019

@author: admaren
"""

from Models import User, Account, Transaction, TransactionModel, UserModel, AccountModel

import npyscreen



class BalEnquiryButtonPress(npyscreen.ButtonPress):
    def whenPressed(self):
        try:
            ano = int(self.parent.accoutno.value)
            val = Account.balenquiry(ano)
            self.parent.ResView.values  = [f"Balance     {val:0.3f}"]
            self.parent.display()
        except ValueError:
            pass

class ListTransactionsButtonPress(npyscreen.ButtonPress):
    def whenPressed(self):
        try:
            ano = int(self.parent.accoutno.value)
            val = Account.balenquiry(ano)
            reslist = Account.showTransactions(int(ano))
            self.parent.ResView.values = reslist
            self.parent.display()
        except:
            pass

class UserHomeViewForm(npyscreen.ActionForm):
    def create(self):
        self.tit = self.add(npyscreen.FixedText, name = "UView", value= "User Views" )
        self.accoutno = self.add(npyscreen.TitleText, name="Enter Account number:", value="")
        self.exitButton = self.add(BalEnquiryButtonPress, name="Balance Enquiry")
        self.lstTransButton = self.add(ListTransactionsButtonPress, name="Transaction list")
        self.ResView = self.add(npyscreen.BoxTitle, name="Query", max_height=6)
        self.ResView.entry_widget.scroll_exit = True
        
    def on_ok(self):
        self.parentApp.change_form("MAIN")
    
    def bal_enquiry(self):
        pass
        
    

_hdr  = "\n"*2 +36*"#" + "\n"*2 
user_home_contents = """
1.balance enquiry
2.deposit
3.withdrawal
4.show transactions
5.edit user details 

Enter x to go back to main view
"""

user_wrong_password_result = "User Not found"



def login_page():
    loginpageview= """
    """
    
    # if login is success
    # got to user_home_....
def user_home_contents_viewfunc():
    
    
    while 1:
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
        elif res1.upper() == "X":
            break
    
def balance_enquiry_func():
    
    daccountno = input("enter your account number :")
    Account.balenquiry(int(daccountno))

def deposit_func():
    daccountno = input("enter your account number :")
    amount = input("enter amount of deposit :")
    Account.deposit(int(daccountno), abs(float(amount)))
    print(f"you have deposited {amount}")

def withdrawal_func():
    accountno = input("enter your account number :")
    wamount = input("enter amount of withdrawal :")
    #amount = input("enter amount of deposit :")
    Account.deposit(int(accountno), -1* float(wamount))
    print(f"you have withdrawed {wamount}")

def show_transactions_func():
    accountno = input("enter your account number :")
    Account.showTransactions(int(accountno))
        

def edit_user_details_func():
    accountno = input("enter your account number:")
    print("your account has been edited ")
    
    
    
    
    
    