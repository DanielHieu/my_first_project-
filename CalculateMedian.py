# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 23:14:06 2019

@author: Vu
"""
# median là só đứng giữa ở ví trí giữa trong dãy số đã sắp xếp

data = [100,60,70,900,100,200,600,500,503,600,1000,1200,700]
def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()
    if N%2==0:
        m1 = N/2
        m2 = N/2 + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) /2
    else:
        middle = (N+1)/2
        middle = int(middle) -1
        median = numbers[middle] 
    return median
median_value = calculate_median(data)
print("Trung vị  số tiền quyên góp là : ",median_value)

