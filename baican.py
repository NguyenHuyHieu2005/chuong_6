# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 18:00:37 2024

@author: ADM
"""

import math
#nhap hai so a,b 
a = float(input("nhap vao gia tri a: "))
b = float(input("nhap vao gia tri b: "))
ab = a*b

#tinh tung gia tri 
can_a = math.sqrt(a)
can_b = math.sqrt(b)
can4_a = math.pow(a,1/4)
can4_b = math.pow(b,1/4)
can4_ab = math.pow(ab,1/4)

#tinh tung phan
phan1 = (can_a - can_b) / (can4_a - can4_b)
phan2 = (can_a + can4_ab) / (can4_a + can4_b)

#ket qua
ket_qua = phan1 - phan2
print(f"ket qua la: {ket_qua}")
# Làm tròn 3 chữ số sau dấu thập phân
number = ket_qua
rounded = round(number, 3)
print(f"kết quả sau khi làm tròn 3 chữ số: {rounded}")