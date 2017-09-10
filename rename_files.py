# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 05:38:14 2017

@author: greul
"""
import os

def rename_files():
    file_list = os.listdir(r"C:\Users\greul\Downloads\prank\prank")
    print (file_list)
    
rename_files()