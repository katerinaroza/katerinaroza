#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:35:03 2021

@author: katerinaroza
"""

##Exercise: Write a Python program to check the validity of password input by users.

import re

def get_password():
    password=input("Please enter your password: ") #gets the password from the user
    return password #returns password

def check_password(password):
    
    length=len(password) #takes the length of the password
    splitted=re.split("", password) #splits password by character
    d=l=s=0 #set initial value as zero for counting for each character type
 
    for x in splitted:            
            if x.isdigit(): #checks if each character of the password is a digit
                d += 1      #if yes,the sum increases by 1 
            elif x.isalpha(): #checks if each character of the password is a letter       
                    l += 1    #if yes,the sum increases by 1 
            elif (x=="$" or x=="#" or x=="@" or x=="!"): #checks if each character of the password is a symbol
                        s += 1 #if yes,the sum increases by 1            
    
    if (length<6 or length>16): #checks the length of the password
        print("ERROR: Your password needs to be between 6-16 characters.") #gives an error if the password length is outside the interval (6,16)
    elif (d==0 or s==0 or l==0): 
        
        if d==0: #if there are no numbers then it gives an error
        
         print("ERROR: Your password need to have at least 1 number")
            
        elif l==0: #if there are no letters then it gives an error
           
          print("ERROR: Your password need to have at least 1 letter")
            
        elif s==0: #if there are no symbols then it gives an error
              
              print("ERROR: Your password need to have at least 1 symbol")
    else:
        
        print("Congrats, your password is valid!")          
              
       
def main_password():
    password=get_password()
    check_password(password)
          
main_password()    
     

