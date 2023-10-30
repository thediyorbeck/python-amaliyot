# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:03:59 2023

@author: user
"""
# import pickle

# with open('pi_million_digits.txt') as file:
#     pi=file.read()
# pi=pi.rstrip()
# pi=pi.replace('\n','')
# pi=pi.replace(' ','')

# # tkun='18122001'
# # print(tkun in pi)

# pi=float(pi)

# with open('pi_float.dat','wb') as fayl:
#     pickle.dump(pi,fayl)

while True:
    kino=input("Sevimli film-serallaringizni kiriting.(to'xtatish uchun-exit deb yozing!)\n")
    if kino!='exit':
        with open('kinolar.txt','a') as file:
            file.write(kino+'\n')
    else:break