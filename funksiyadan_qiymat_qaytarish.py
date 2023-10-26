# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:33:04 2023

@author: user
"""

def f_info(ismi, familiyasi, t_yili, t_joyi, emaili='', telraqam=None):
    foydalanuvchilar={
        'ism':ismi,
        'familiya':familiyasi,
        't_yil':t_yili,
        't_joy':t_joyi,
        'email':emaili,
        'telraqam':telraqam
        }
    return foydalanuvchilar

# foydalanuvchi1=f_info('Diyorbek', 'Ganjayev', 2001, 'Xorazm')
# foydalanuvchi2=f_info('Sardor', 'Axmedov', 1999, 'Xorazm', telraqam=905590899)
# shaxslar=[foydalanuvchi1,foydalanuvchi2]

print("Foydalanuvchilar ro'yxatini yaratamiz:")
shaxslar=[]
while True:
    ismi=input('Foydalanuvchi ismini kiriting: ')
    familiyasi=input('Foydalanuvchi familiyasi: ')
    t_yili=input("Tug'ilgan yil: ")
    t_joyi=input("Tug'ilgan joyi: ")
    emaili=input("Elektron pochta manzili: ")
    telraqam=input('Telefon raqami: ')
    shaxslar.append(f_info(ismi, familiyasi, t_yili, t_joyi, emaili, telraqam))
    javob=input("Yana ma'lumot qo'shasizmi?")
    if javob=="yo'q":
        break
    

def kattasini_top(son1,son2,son3):
    """3 ta sondan kattasini topadigan funksiya"""
    if son1>son2:
        if son1>son3:
            return son1
        else:
            return son3
    elif son2>son3:
        return son2
    else:
        return son3
    
a= kattasini_top(13,26,4)
print(a)

def radius(r):
    aylana={
        'radius': r,
        'diametr':2*r,
        'perimetr': 2*3.14*r,
        'yuza':3.14*r*r
        }
    return aylana

r=float(input('Aylana radisuini kiriting: '))
print(radius(r))

    
def tubsonlar(a, b):
    """a-boshi, b-oxiri"""
    sonlar=[]
    for n in range(a, b+1):
        tub=True
        if n==1: 
            tub=False
        elif n==2:
            tub=True
        else: 
            for x in range(2,int(n**0.5)+1):
                if n%x==0:
                    tub=False
        if tub: 
            sonlar.append(n)
        
    return sonlar

print(tubsonlar(2,4))

def fibonachchi(n):
    sonlar=[]
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else: sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonachchi(8))

