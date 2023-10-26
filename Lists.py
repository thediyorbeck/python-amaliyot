# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:42:03 2023

@author: user
"""
#amaliyot1
# ismlar = ['Abror', 'Sardor', 'Fozil', 'Jasur']
# print(ismlar[0]+" qarzimni ertaga beraman, xavotirlanma")
# print(ismlar[1]+ " og'o kettik ko'chaga")
# print(ismlar[2]+ " ps o'ynisanmi?")
# print(ismlar[3]+ " nima gap oshna")

#amaliyot2
# t_shaxslar=["Stiv Jobs", 'Alan Turing', 'Nikola Tesla', 'Zigmund Freyd']
# z_shaxslar=["Mark Zukerberg", 'Elon Musk', 'Jack Dorsi', 'Backham']
# print("Men tarixiy shaxslardan", t_shaxslar.pop(-1)," va zamonaviy shaxslardan"
#      , z_shaxslar.pop(3)," bilan ko'rishishni xohlayman")

#amaliyot3
friends=[]
friends.append("Jamshid")
friends.append("Akmal")
friends.append("Zoir")
friends.append("Shohruh")
friends.append("Bekturdi")
friends.append("Bekzod")
friends.append("Islom")
friends.remove("Zoir")
friends.remove("Shohruh")
friends.remove("Bekzod")
friends.insert(0, "Zafar")
friends.insert(2, "Shahzod")
friends.append("Umid")
mehmonlar=[]
mehmonlar.append(friends.pop(4))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(2))

print("Kelgan mehmonlar: ", mehmonlar, "\nKela olmagan do'stlarim: ", friends)
