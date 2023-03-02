# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:17:02 2023

@author: answl
"""

import pandas as pd

student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90, '영어':80})

'''
헐 이렇게는 안됨
print(student1 + '\n')
print(student2 + '\n')
'''

print(student1, '\n')
print(student2, '\n')

addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2

print(type(division))
print('\n')

result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(result)

#               국어        수학      영어
# 덧셈    190.000000   170.000   160.0
# 뺄셈     10.000000    10.000     0.0
# 곱셈   9000.000000  7200.000  6400.0
# 나눗셈     1.111111     1.125     1.0

