# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 22:30:52 2019

@author: Vu
"""

def giaiThua(n):
    if(n==1):
        return n
    return n*giaiThua(n-1)
def estimate(number):
    result = 0
    for i in range(1,number+1):
        result = result +  i / giaiThua(i)
    return result
n = int(input("input number : "))
print(estimate(n))
