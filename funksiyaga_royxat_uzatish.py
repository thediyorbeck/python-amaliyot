# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:37:38 2023

@author: user
"""

# def kattaharf(matnlar):
#     matnlar=matnlar[:]
#     for n in range(len(matnlar)):
#         matnlar[n]=matnlar[n].capitalize()
#     return matnlar
# kitoblar=['jek va loviya poyasi','oq kema','gulliverning sarguzashtlari',"sariq devni minib"]
# yangi_kitoblar=kattaharf(kitoblar)
# print(yangi_kitoblar)
# print(kitoblar)
        
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho=input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism.title()]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)