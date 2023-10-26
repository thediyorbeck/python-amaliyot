# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:25:47 2023

@author: user
"""

buyurtmalar=[]
savol="Buyurtma qiling: "
while True:
    buyurtma=input(savol)
    buyurtmalar.append(buyurtma)
    sikl=input("yana buyurtma qilasizmi? (ha yoki yo'q)")
    if sikl=='ha':
        continue
    else: break


savat={}
while True:
    mahsulot=input("Mahsulot nomi: ")
    narx=input(f"{mahsulot}ni narxi: ")
    savat[mahsulot]=narx
    takrorla=input("yana mahsulot qo'shashizmi?(ha yoki yo'q) ")
    if takrorla=='ha':
        continue
    else: break

for taom in buyurtmalar:
    if taom in savat:
        print(f"\n{taom} ning narxi: {savat[taom]} so'm")
    else: print(f"Bizda {taom} yo'q")