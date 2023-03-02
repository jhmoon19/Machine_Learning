# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:28:13 2023

@author: answl
"""

import pandas as pd
import numpy as np

student1 = pd.Series({'국어': np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})

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

#      국어        수학  영어
# 덧셈  NaN   170.000 NaN
# 뺄셈  NaN    10.000 NaN
# 곱셈  NaN  7200.000 NaN
# 나눗셈 NaN     1.125 NaN