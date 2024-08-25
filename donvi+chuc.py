# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:37:35 2024

@author: ADM
"""
while True:
    #Nhập vào số nguyên N có 2 chữ số 
    N = int(input("nhập số nguyên N có 2 chữ số: "))

    #kiểm tra lại có phải nhập 2 chữ số không 
    if N < 10 or N > 99:
        print("lưu ý! hãy nhập số có 2 chữ số")

    else:
        #lấy chữ số hàng chục,đơn vị 
        chuc = N // 10 
        donvi = N % 10 
        #lấy hàng chục cộng hàng đơn vị 
        dapan = chuc + donvi
        #in kết quả ra màn hình 
        print(f"kết quả : {chuc} + {donvi} = {dapan}")
        user_input = input("Nhấn Enter để tiếp tục nhập số khác (hoặc 'a' để thoát): ")
        if user_input.lower() == 'a':
            break

