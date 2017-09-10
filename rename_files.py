# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 05:38:14 2017

@author: greul
"""
import os

def rename_files():
    file_list = os.listdir(r"C:\Users\greul\Downloads\prank\prank")
    print (file_list)
    os.chdir(r"C:\Users\greul\Downloads\prank\prank")
    translation_table = dict.fromkeys(map(ord, '0123456789'), None)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(translation_table))
    
rename_files()