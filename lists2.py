# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:33:57 2023

@author: user
"""

#davlatlar=["Fransiya", "Germaniya", "Kanada", "AQSh", "Yaponiya", "Norvegiya"]
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
#davlatlar.sort(reverse=True)

# juft_sonlar=list(range(120,1200,2))
# print(sum(juft_sonlar))
# print(len(juft_sonlar))
# print(max(juft_sonlar)-min(juft_sonlar))
# print(juft_sonlar[:20], juft_sonlar[270:290], juft_sonlar[520:])

taomlar=['manti', 'osh', 'chuchvara', 'shirguruch', 'shashlik']
nonushta=taomlar[:]
del nonushta[:2]
del nonushta[-1]
nonushta.append("mastava")
nonushta.append("shivit osh")

print(taomlar)
print(nonushta)

# nonushta= tuple(nonushta)
# nonushta[0]='pitsa'            #tuple ro'yxatni o'zgarmas qildi, bu amal bajarilmaydi
