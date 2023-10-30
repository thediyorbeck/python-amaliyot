# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:08:59 2023

@author: user
"""
import json
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_json=json.dumps(data)

# talaba='{"ism":"Hasan","familiya":"Husanov","tyil":2000}'
# with open('talaba.json','w') as file:
#     file.write(talaba)
    
# filename='talaba.json'

# with open(filename) as f:
#     talabalar=json.load(f)
# print(f"Ismi: {talabalar['ism']}, familiyasi: {talabalar['familiya']}")

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba=json.loads(talaba_json)
with open('talaba_ismi.json','w') as f:
    f.write(talaba['ism'])
with open('talaba_familiyasi.json', 'w') as fayl:
    fayl.write(talaba['familiya'])