# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:35:39 2023

@author: user
"""

import datetime as dt
import re

bugun=dt.date.today()
# print(bugun)
for n in range(10):
    print(bugun+dt.timedelta(weeks=n*2))

# today=dt.date.today()
# ramazon=dt.date(2024,4,9)
# farq=ramazon-today
# print(f"Ramazongacha {farq.days} kun qoldi")

# tkun=dt.date(2022,12,18)
# bugun=dt.date.today()
# farq=bugun-tkun
# oy=int(farq.days/30)
# kun=int(farq.days%30)
# print(f"Tug'ilgan kunimdan beri {oy} oyu, {kun} kun o'tdi")

    
# andoza="^[\+][(]?[0-9]{3}[)]?[-\s\.]?[0-9]{2}[-\s\.]?[0-9]{7}$"
# while True:
#     telraqam=input("Telefon raqamingizni kiriting: ")
#     if re.match(andoza,telraqam):
#         print("Raqamingiz muvaffaqqiyatli qabul qilindi.")
#         break
#     else:
#         print("Raqam noto'g'ri kiritilgan!")