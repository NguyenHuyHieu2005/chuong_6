# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:19:23 2024

@author: ADM
"""

#nhap chuoi ban dau
chuoi = "Đại học Quốc Gia , Khu phố 6 , P. Linh Trung , Q. Thủ Đức , Tp. Hồ Chí Minh"
#tách chuỗi 
chuoia = [s.strip() for s in chuoi.split(",")]

#danh sach 1
danhsach1 = chuoia

#damhsach2
chuoi= chuoi.replace("P. ", "").replace("Q. ", "").replace("Tp. ", "")
chuoi = [s.strip() for s in chuoi.split(",")]
#in danh sach
print("Danh sách 1:")
for item in danhsach1:
    print(item)
print("Danh sách 2:")
for item in chuoi:
    print(item)
