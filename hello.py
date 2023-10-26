# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 01:01:43 2021

author: diyorbek
"""
ismlar=["Jasur", "Shohjahon", "Aziz", "Avaz", "Isroil", "Akmal", "Botir"]
friends = ["Fozil", "Iqbol"]
ismlar.insert(4, "Abdulla")
ismlar.append(friends[-1])
#del ismlar[0:5]
ismlar.sort()

sonlar = [3,4,12,15,96,7341,24,55,35,-8,-95,-6.3]
#print(sorted(sonlar, reverse=True))
#print(min(sonlar))
sonlar.reverse()
#print(sonlar)
a=len(sonlar)
#print(sonlar[a-5])

#Range funksiyasi

#yosh= list(range(0,24))
#print(yosh)
print(ismlar[5])