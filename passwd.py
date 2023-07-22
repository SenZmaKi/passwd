#!/usr/bin/python
# This script is used to generate a password from a select parameter

import random
import string
import sys
import time

# get the parameter(length and chars) from the user
def getParams():
    print ("Please select the level of security you would like :")
    print ("1. Basic (length = [8 chars] letters)")
    print ("2. Standard (length = [10 chars] letters and numbers)")
    print ("3. Fort Knox (length = [15 chars] letters, numbers and symbols)")
    print ()

    selection = input("Please enter your selection: ")
    
    if selection == "1":
        length = 8
        chars = string.ascii_letters
        print ("You have selected Basic")
    elif selection == "2":
        length = 10
        chars = string.ascii_letters + string.digits
        print ("You have selected Standard")
    elif selection == "3":
        length = 15
        chars = string.ascii_letters + string.digits + string.punctuation
        print ("You have selected Fort Knox")
    else:
        print ("Invalid selection, please try again")
        getParams()
    
    return length, chars

def generatePassword(length, chars):
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

