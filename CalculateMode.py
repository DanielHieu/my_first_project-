# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 23:32:05 2019

@author: Vu
"""
# mode trả về phần từ có số lần xuất hiện nhiều nhất
from collections import Counter
points = [7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,9,4,2,5,5,5,5,5,9,6]
def calculate_mode(numbers):
    # hàm counter để đếm số lần xuất hiện của mỗi phần tử
    c = Counter(numbers)
    # hàm most_common truyền tham số 1 vào trả về giá trị và số lần phần từ xuất hiện nhiều nhất
    mode = c.most_common(1)
    return mode[0][0]
#print('Mode của chuổi số dã cho : ',calculate_mode(points))
def calculate_modes(numbers):
    c = Counter(numbers)
    # hàm most_common trả về 1 tuple (giá trị , số lần xuất hiện)
    number_freg = c.most_common()
    max_count  = number_freg[0][1]
    result=[]
    for num in number_freg:
        if num[1] == max_count:
            result.append(num[0])
    return result
#print('Mode của chuổi số đã cho là: ',calculate_modes(points))
def print_Table_freg(numbers):
    c = Counter(numbers)
    number_freg = c.most_common()
    print('Number\tFrequency')
    for num in number_freg:
        print('{0}\t{1}'.format(num[0],num[1]))
print_Table_freg(points)