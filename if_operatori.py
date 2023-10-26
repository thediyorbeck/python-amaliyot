# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:14:36 2023

@author: user
"""

# cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car!='gm':
#         print(car.title())
#     else:
#         print(car.upper())

# foydalanuvchi_ismi=input("Login: ")
# if foydalanuvchi_ismi=='admin':
#     print("Xush kelibsiz, ", foydalanuvchi_ismi.title(), ", foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"{foydalanuvchi_ismi.title()}, Xush kelibsiz!")

print("Ikkita son kiriting:")
son1=float(input("Birinchi son: "))
son2=float(input("Ikkinchi son: "))
if son1>son2:
    print("1-son katta")
else: 
    if son1<son2:
        print("2-son katta")
    else:
        print("sonlar teng")