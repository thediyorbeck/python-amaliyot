# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:54:18 2023

@author: user
"""

# ismlar= ['Durdona', 'Barno', 'Mushtariy', 'Shuhrat', 'Nodir']
# for ism in ismlar:
#     print("Salom, ", ism)
    
# print("Kod",len(ismlar),"marta takrorlandi.")

# sonlar=list(range(11,100,2))
# kublar=[]
# for son in sonlar:
#     kublar.append(son**3)
    
# print(kublar)

# kinolar=[]
# print("Eng sevimli 5 ta filming:")
# for n in range(1,6):
#     kinolar.append(input(f"{n}. "))
    
# print(kinolar)

n_kishilar=int(input("Bugun nechta odam bilan ko'rishdingiz? "))
ismlar=[]
for n in range(n_kishilar):
    ismlar.append(input(f"{n+1}. "))
    
print(ismlar)
