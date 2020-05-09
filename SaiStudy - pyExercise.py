#!/usr/bin/env python
import collections
import sys
def sort1(nums):
    return list(dict.fromkeys(nums))

def interpret(value, commands, args):
    j = 0
    for k in commands:
        if k == '+':
            if j == 0:
                output = value + args[j]
            else: output = output + args[j]
        elif k == '-':
            output = value - args[j]
        elif k == '*':
            output = value * args[j]
        else:
            return 1
        j = j + 1
    return output

if __name__== "__main__":
    mylist = sort1([1,3,5,7,7])
    mylist.sort()
    print(mylist)
    mylist = sort1([11,3,5,7,7])
    mylist.sort()
    print(mylist)
    b = interpret(1,['+','+'],[4,5])
    print(b)