#!/usr/bin/env python
import collections
import sys
def sleep_in(weekday, vacation):
    if weekday in ("monday", "tuesday", "wednesday", "thursday", "friday"):
        print("go to work")
    else:
        if weekday in ("saturday", "sunday"):
            print("its vacation")
def first_last6(nums):
    x = len(nums) -1
    if(nums[0] == 6 or x == 6 ):
        print("True")
    else:
        print("false")

def same_first_last(nums):
    x = len(nums)
    a = nums[0]
    b = len(nums) - 1
    if x > 1:
        if a == b:
            print("True")
        else:
            print("False")

def make_pi():
    a = {3,1,4}
    return a

def sum(nums):
    b = 0
    for a in nums:
        b = b + a
    return b
def count_hi(str):
    chk = "hi"
    count = str.count(chk)
    return count
def count_evens(nums):
    count = 0
    for i in nums:
        j = i % 2
        if j == 0:
            count = count + 1
    return count
def count_int(nums):
    count = 0
    for i in nums:
        if i.isnumeric() == True:
            d = int(i)
            count = count + d
    return count
if __name__== "__main__":
    sleep_in("saturday","xyz")
    first_last6([1,4,5])
    first_last6([6,3,4,5])
    same_first_last([1,4,6,1])
    same_first_last([1,4,6,7])
    same_first_last([1])
    b = make_pi()
    print(b)
    c = sum({1,3,7})
    print(c)
    d = count_hi("str hi str hi hi ste")
    print(d)
    e = count_evens([3,4,5,6,7,8])
    print(e)
    f= count_int("str 234 str 123")
    print(f)
    #
