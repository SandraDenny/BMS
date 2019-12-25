#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:40:11 2019

@author: admaren
"""
import sys
import npyscreen


sys.path.append("/home/admaren/Documents/BankManagementSys")
from Views.welcome import Welcome_contents, MainForm
from Views.UserHomeView import user_home_contents_viewfunc, UserHomeViewForm
from Views.manageaccountview import manage_account_viewfunc, ManageAccountForm, AddNewUserForm



class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        # When Application starts, set up the Forms that will be used.
        # These two forms are persistent between each edit.
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        self.addForm("MAIN", MainForm, name="Banking Management System", color="IMPORTANT",)
        self.addForm("USER", UserHomeViewForm, name="User View")
        self.addForm("AMAN", ManageAccountForm, name="Manage Account")
        self.addForm("NUSER", AddNewUserForm,name="Add new User")
       
            
    def onCleanExit(self):
        npyscreen.notify_wait("Goodbye!")
    
    def change_form(self, name):
        # Switch forms.  NB. Do *not* call the .edit() method directly (which 
        # would lead to a memory leak and ultimately a recursion error).
        # Instead, use the method .switchForm to change forms.
        self.switchForm(name)
        
        # By default the application keeps track of every form visited.
        # There's no harm in this, but we don't need it so:        
        self.resetHistory()



def main():
    TA = MyTestApp()
    TA.run()


if __name__ == '__main__':
    main()

# while 1:

#     user_ans1 = input(Welcome_contents)
    
#     if user_ans1=="1":
#         manage_account_viewfunc()
    
#     if user_ans1 == "2":
#         user_home_contents_viewfunc()
        
#     if user_ans1 == "x":
#         break
        

