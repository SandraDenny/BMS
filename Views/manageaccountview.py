#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:01:11 2019

@author: admaren

"""

import sys
import npyscreen

sys.path.append("/home/admaren/Documents/BankManagementSys")

_hdr  = "\n"*2 +36*"#"+"\n"*2 

from Models import User, Account, Transaction

class AddUserButtonPush(npyscreen.ButtonPress):
    def whenPressed(self):
        
        u = User()
        u.Name = self.parent.uname.value
        u.Address = self.parent.address.value
        u.DOB = self.parent.dob.value
        
        umodel = u.AddToDB()
        
        amt = float(self.parent.initamount.value)
        
        atype = "SAVINGS"
        if self.parent.aType.values[0] == 0:
            atype = "SAVINGS"
        if self.parent.aType.values[0] == 1:
            atype = "CURRENTS"
        
        
        amodel = Account.AccountAddToDB(umodel, atype)
        
        # amt = float(self.initamount.value)
        t0 = Transaction()
    
        t0.amount = float(amt)
        t0.addTransactionToDB(amodel)

class ListUserButtonPuse(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.ResView.values = User.ListUsers()
        self.parent.display()

class AddNewUserForm(npyscreen.ActionFormV2):
    def create(self):
        self.uname = self.add(npyscreen.TitleText, name ="User Name")
        self.address = self.add(npyscreen.TitleText, name ="Address")
        self.dob = self.add(npyscreen.TitleDateCombo, name="DOB")
        self.initamount = self.add(npyscreen.TitleText,\
                                   name="Inital Deposit amout",
                                   value ="500.0")
        self.aType = self.add(npyscreen.TitleSelectOne, max_height=4,
                              name="Account Type",
                              scroll_exit= True, \
                                  values=["SAVINGS", "CURRENT"])
        self.AddUser = self.add(AddUserButtonPush, name="Add User")
    
    def on_cancel(self):
        self.parentApp.change_form("AMAN")


class ManageAccountForm(npyscreen.ActionForm):
    def create(self):
        self.title = self.add(npyscreen.FixedText,
                              name="title", value ="Account management")
        self.chosen = self.add(npyscreen.TitleSelectOne,
                               max_height=6,
                               scroll_exit = True,\
                               name="AChoice", \
                                   values =["Add New Account", "Close Account"])
        self.res = self.add(ListUserButtonPuse, name="List users")
        self.ResView = self.add(npyscreen.BoxTitle, name="Query Result")
    
    def on_cancel(self):
        self.parentApp.change_form("MAIN")
    
    def on_ok(self):
        if self.chosen.value[0] == 0:
            self.parentApp.change_form("NUSER")


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

    
    
    
    
    
        
        
    


        
    