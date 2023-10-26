# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:56:58 2023

@author: user
"""

# def kopaytir(*sonlar):
#     kopaytma=1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma

#print(kopaytir(21,13,12,6,5,4,0))

def talaba_info(ism, familiya, **malumotlar):
    malumotlar["ism"]=ism
    malumotlar['familiya']=familiya
    return malumotlar

talaba1=talaba_info('Aziz','Saidkamolov',yoshi=16,manzil="Muborak tumani")
talaba2=talaba_info('Nodir', 'Davronov', yoshi=9, manzil='Qarovul qishloq')

talabalar=[talaba1,talaba2]