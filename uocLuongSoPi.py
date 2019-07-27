# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 22:18:17 2019

@author: Vu
"""

import math
import random

# tong so diem p duoc sinh ra
N = 100000
# số điểm thuộc đường tròn
N_T = 0

for _ in range(N):
    # sinh số ngẫu nhiên trong khoảng [-1,1]
    x = random.randint(-1,1)
    y = random.randint(-1,1)
    
    x2 = x**2
    y2 =y**2
    # công thức tính đường tròn
    # kiểm tra p có nằm trong đường tròn không
    if math.sqrt(x2 + y2) <=1.0:
        N_T = N_T + 1
pi = (N_T/N) *4
print(pi)

