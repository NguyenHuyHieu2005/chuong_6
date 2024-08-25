# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:53:04 2024

@author: ADM
"""

a = float(input("nhap so thu nhat: "))
b = float(input("nhap so thu hai: "))

tong = a + b 
hieu = a - b 
tich = a * b 
thuong = a / b 
du = a % b 
nguyen = a // b 

print(f"tổng là: {tong}")
print(f"hiệu là: {hieu}")
print(f"tích là: {tich}")
print(f"chia lấy phần dư là: {du}")
print(f"chia lấy phần nguyên là: {nguyen}")
# Làm tròn 2 chữ số sau dấu thập phân
number = thuong
rounded_2 = round(number, 2)
print(f"Số sau khi làm tròn 2 chữ số: {rounded_2}")

# Làm tròn 3 chữ số sau dấu thập phân
number = thuong
rounded_3 = round(number, 3)
print(f"Số sau khi làm tròn 3 chữ số: {rounded_3}")