# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:50:43 2023

@author: user
"""

# pythonizoh={
#     'integer':'butun sonlar',
#     'float':'haqiqiy sonlar',
#     'string':'matnli qiymat',
#     'for':'takrorlanuvchi sikl',
#     'if':'agar operatori',
#     'elif-else':"shartlar ko'p bo'lganda ishlatiladi",
#     'list':"ro'yxat",
#     'append':"ro'yxatga yangi element qo'shish metodi, ro'yxatni doim oxiriga qo'shadi",
#     'insert':"ro'yxatni istalgan joyiga indeks orqali element qo'shish",
#     'remove':"ro'yxat elementlarini o'chirish metodi",
#     'del':"bu funksiya ham elementlarni o'chirish uchun ishlatiladi, indeks orqali",
#     'pop':"ro'yxat elementini indeks orqali qayergadir olib turish uchun ishlatiladi"    
#     }

# # for k,q in sorted(pythonizoh.items()):
# #     print(f"'{k}' atamasiga ta'rif: - {q}\n")

# pythonizoh['set']="lug'atdagi dublikat qiymatlarni o'chiradi"

# soz=input("Qidirmoqchi bo'lgan so'zingizni yozing: ")
# print(pythonizoh.get(soz,'bunday so\'z lug\'atimizda yo\'q'))

taomlar = {
    'osh': 25,
    'manti': 30,
    'shashlik': 14,
    "lag'mon": 20,
    'somsa': 8,
    'qozon kabob': 35,
    'qaymoq': 10,
    'choy': 2,
    'salat': 7,
    'non': 3,
    'kola':12,
    'fanta':10,
    'kompot':8
    }

royxat=[]
narx=0
yoqroyxat=[]
print("Buyurtma bering:")
for n in range(1,6):
    royxat.append(input(f"{n}. "))
    
for taom in royxat:
    if taom in taomlar.keys():
        narx=narx+taomlar[taom]
    else:
        yoqroyxat.append(taom)

print(f"\nBuyurtmangiz {narx} ming so'm bo'ldi")
if yoqroyxat:
    print(f"Mana bular esa bizda yo'q: {yoqroyxat}")        
    
    
    
    
    
    
    
    
    
    