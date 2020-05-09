#!/usr/bin/env python
import collections
import sys

    #
print("The topic is movies::")
secret = "spectre"
iw = len(secret)
b= 0
while b <= 2:

    print("The no of chars ou have to guess is ", iw)
    a = 0
    c = 0
    for i in range(0,6):
        opt = input("Please enter your char::")
        if opt in secret:
            a+=1
            print(opt)
        else:
            c+=1
            print("_")
        if a == 6:
            print("Sucess")
            exit(0)
        if c == 6:
            print("Try 1 down")
            b+=1