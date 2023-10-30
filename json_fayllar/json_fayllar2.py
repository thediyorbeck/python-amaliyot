# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:07:29 2023

@author: user
"""

import json

with open('students.json') as f:
    student=json.load(f)
    
# student_json=json.dumps(student, indent=4)
# print(student_json)

for n in range(3):
    print(f"Ismi: {student['student'][n]['name']}",
          f"Familiyasi: {student['student'][n]['lastname']}",
          f"{student['student'][n]['year']}-kurs",
          f"{student['student'][n]['faculty']} fakulteti talabasi")