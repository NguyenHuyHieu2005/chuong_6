# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:12:35 2024

@author: ADM
"""

chuoi = "im a cat"

chuoi1 = chuoi.replace("im", "Im").replace("a", "A").replace("cat", "Cat")
chuoi2 = chuoi.replace("im", "IM").replace("a", "A").replace("cat", "CAT")
chuoi3 = chuoi.replace("im", "iM").replace("cat", "cAT")
chuoi4 = chuoi
print(chuoi1)
print(chuoi2)
print(chuoi3)
print(chuoi4)
