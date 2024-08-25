# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:12:45 2024

@author: ADM
"""

# In menu trực tiếp
print("============ MENU ============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("==============================")

# Nhập lựa chọn 
lua_chon = input("Moi nhap lua chon: ")
print("==============================")

# Xử lý lựa chọn
if lua_chon == '1':
    print("Ban da chon Hu tieu")
elif lua_chon == '2':
    print("Ban da chon Chao long")
elif lua_chon == '3':
    print("Ban da chon Banh canh")
elif lua_chon == '4':
    print("Ban da chon Bun rieu")
elif lua_chon == '5':
    print("Ban da chon Pho bo")
else:
    print("Lua chon khong hop le!")