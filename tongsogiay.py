# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:07:12 2024

@author: ADM
"""
 # Nhập vào thời gian theo định dạng hh:mm:ss
time_input = input("Nhập vào giờ, phút và giây (định dạng hh:mm:ss): ")
hh , mm , ss = map(int , time_input.split(":"))
# Kiểm tra xem giờ, phút, giây có hợp lệ không
if 0 <= hh <= 24 and 0 <= mm < 60 and 0 <= ss < 60:
         # Đổi giờ, phút, giây ra giây
         total_seconds = hh * 3600 + mm * 60 + ss

         # In kết quả ra màn hình
         print(f"Tổng số giây: {total_seconds}")
else:
    print(" giờ phút hoặc giây không hợp lệ.")