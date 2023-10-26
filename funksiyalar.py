# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:57:49 2023

@author: user
"""

def yil_hisobla(ism, yosh):
    """Foydalanuvchi ismi va yoshini so'rab, tug'ilgan yilini
    hisoblaydigan funksiya"""
    print(f"Salom {ism}, siz {2023-yosh}-yilda tug'ilgansiz.")
    
# ism=input('Ismingiz: ')
# yosh=int(input('Yoshingiz: '))

# yil_hisobla(ism,yosh)

def juft_toq(son):
    """Foydalanuvchidan son olib juft yoki toqligini tekshiradigan funksiya"""
    if son%2==1:
        print('Toq son')
    else: print("Juft son")
    
def bolinmanitekshir(son):
    """Sonni 2 dan 10 gacha bo'lgan sonlardan qaysi biriga 
    qoldiqsiz bo'linishini tekshiradigan funksiya"""
    for n in range(2,11):
        if son%n:
            print(f"{son} {n} ga qoldiqli bo'linadi")
        else: print(f"{son} {n}ga qoldiqsiz bo'linadi")
