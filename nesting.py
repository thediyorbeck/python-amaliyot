# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:51:05 2023

@author: user
"""

# nolan={
#        'ism':'Kristofer Nolan',
#        'yil':1970,
#        'joy':'London, Angliya',
#        'janr':'Ilmiy fantastika',
#        'asar':'Interstellar, Inception, The Dark Knight'
#        }
# tarantino={
#     'ism':'Kventin Tarantino',
#     'yil':1963,
#     'joy':'Tennesi, AQSh',
#     'janr':'Vestern',
#     'asar':'Pulp Fiction, Kill Bill, Django: Unchained '
#     }
# fincher={
#     'ism':'David Fincher',
#     'yil':1962,
#     'joy':'Kolorado, AQSh',
#     'janr':'Detektiv, prixologik triller',
#     'asar':'Fight club, Seven, Social Network'
#     }
# vilnyov={
#     'ism':'Deni Vilnyov',
#     'yil': 1967,
#     'joy':'Jantiyi, Kanada',
#     'janr':'Triller, ilmiy fantastika',
#     'asar':'Enemy, Prisoners, Dune'
#     }

# kino=[nolan, tarantino, fincher, vilnyov]
# print("Mening sevimli kinorejissyorlarim:\n")
# for rej in kino:
#     ism=rej['ism']
#     yil=rej['yil']
#     joy=rej['joy']
#     janr=rej['janr']
#     asar=rej['asar']
#     print(f"{ism}ning mashhur filmlari quyidagilar: {asar} \n")


# kino={
#       "Ahmad":['Shoushenkdan qochish', 'Forrest Gamp', "Cho'qintirgan ota"]
      
#       }

dostlar={
    'Ahmad':[],
    'Ibrat':[],
    'Abror':[]
    }
# kinoroyxat=[]
for dost in dostlar.keys():
    print(f"\n{dost} 3 ta sevimli kino-serialingizni sanang:")
    for n in range(1,4):
        dostlar[dost].append(input(f"{n}- "))
print("\nDemak,")

for ism,kinolar in dostlar.items(): 
    print(f"\n{ism}ning sevimli kino-seriallari: ")
    for kino in kinolar:  
        print(kino)

