# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:56:25 2024

@author: ADM
"""
# nhập giá trị a, b, c 
a = int(input("nhap so thu nhat: "))
b = int(input("nhap so thu hai: "))
c = int(input("nhap so thu ba: "))

#kiểm tra xem có phải phương trình bậc 2 không 
if a == 0:
    print("đây không phải là phương trình bậc hai ")
else:
    # tạo chuỗi cho phương trình 
    print(f"{a}X^2 + {b}x + {c} = 0")