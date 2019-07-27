# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 23:05:27 2019

@author: Vu
"""
def calculate_mean(numbers):
    s = sum(numbers)
    n = len(numbers)
    mean = s/n
    return mean
donations = [100,60,70,90,80,500]
mean_value = calculate_mean(donations)
print('Trung bình số tiền quyên góp là: ',mean_value)
