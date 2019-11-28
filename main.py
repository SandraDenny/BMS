#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:40:11 2019

@author: admaren
"""

from Views.welcome import Welcome_contents
from Views.UserHomeView import user_home_contents_viewfunc
from Views.manageaccountview import manage_account_viewfunc


user_ans1 = input(Welcome_contents)

if user_ans1=="1":
    manage_account_viewfunc()

if user_ans1 == "2":
    user_home_contents_viewfunc()

