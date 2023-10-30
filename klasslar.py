# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:22:31 2023

@author: user
"""



class User:
    def __init__(self,ism,familiya,nickname,email):
        self.ism=ism
        self.familiya=familiya
        self.email=email
        self.nickname=nickname
        
    def fullname(self):
        return f"{self.ism} {self.familiya}"
    
    def yosh_hisobla(self,tyil):
        return f"{2023-tyil} yoshda"
        
    def tanishtir(self):
        print(f"Foydalanuvchi: {self.nickname}, ismi: {self.ism} {self.familiya}, email: {self.email}")
        
user1=User('Diyorbek','Ganjayev','thediyorbeck','diyorbekganjayev001@gmail.com')

print(user1.fullname())
print(user1.yosh_hisobla(2001))
