# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:31:02 2023

@author: user
"""

# kitob=""
# while kitob!='exit':
#     kitob= input("Yaxshi ko'rgan kitoblaringizni kiriting: ")

# savol='Yoshingizni kiriting: '
# while True :
#     yosh=input(savol)
#     if yosh=="exit" or yosh=="quit":
#         break
#     yosh=int(yosh)
#     if yosh<7:
#         print("Chipta narxi : 2000 so'm")
#     elif yosh<18:
#         print("Chipta narxi: 5000 so'm")
#     elif yosh<65: 
#         print("Chipta narxi: 10000 so'm")
#     else: print("Sizga bepul!")
    

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")