#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:35:03 2021

@author: katerinaroza
"""

##Exercise: Write a Python program to check the validity of password input by users.

import re

def get_password():
    password=input("Please enter your password: ")
    return password

def check_password(password):
    
    length=len(password)
    splitted=re.split("", password)
    d=l=s=0
 
    for x in splitted:            
            if x.isdigit():
                d += 1
            elif x.isalpha():         
                    l += 1
            elif (x=="$" or x=="#" or x=="@"):
                        s += 1
    
    if (length<6 or length>16):
        print("ERROR: Your password needs to be between 6-16 characters") 
    elif (d==0 or s==0 or l==0): 
        
        if d==0:
        
         print("ERROR: Your password need to have at least 1 number")
        elif l==0:
           
          print("ERROR: Your password need to have at least 1 letter")
        elif s==0:
              
              print("ERROR: Your password need to have at least 1 symbol")
    else:
        
        print("Congrats, your password is valid!")          
              
       
def main_password():
    password=get_password()
    check_password(password)
          
main_password()    
     

