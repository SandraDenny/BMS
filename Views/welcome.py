#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:40:05 2019

@author: admaren
"""

import npyscreen

Welcome_contents ="""

 ____   __  __    _____ 
|  _ \ |  \/  |  / ____|
| |_) || \  / | | (___  
|  _ < | |\/| |  \___ \ 
| |_) || |  | |_ ____) |
|____(_)_|  |_(_)_____/ 


1. Manage Accounts
2. User Accounts

Enter x to quit!!

"""

class MainForm(npyscreen.ActionForm):
    def create(self):
        #self.add(npyscreen.TitleText, name = "Text:", value= "Press ^T to change screens" )
        self.add(npyscreen.FixedText, value= "Welcome to banking management system")
        self.chosen = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3,\
                               name='GOTO', values = ['Manage  Accounts', 'Manage Users'])
        #self.add
        
        # self.add_handlers({"^T": self.change_forms})

    def on_ok(self):
        # Exit the application if the OK button is pressed.
        #self.parentApp.switchForm(None)
        print(f"chosen value {self.chosen.value}")
        # raise Exception(self.chosen.value)
        if self.chosen.value[0] == 1:
            #raise Exception(self.chosen.value)
            self.parentApp.change_form("USER")

    # def change_forms(self, *args, **keywords):
    #     if self.name == "Screen 1":
    #         change_to = "SECOND"
    #     elif self.name == "Screen 2":
    #         change_to = "THIRD"
    #     else:
    #         change_to = "MAIN"

    #     # Tell the MyTestApp object to change forms.
    #     self.parentApp.change_form(change_to)
    

