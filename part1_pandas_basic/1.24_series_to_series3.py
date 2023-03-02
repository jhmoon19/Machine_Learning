# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:30:43 2023

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

# NaN 피하기: 연산 메소드의 fill_value=0 옵션 이용
add = student1.add(student2, fill_value=0)
sub = student1.sub(student2, fill_value=0)
mul = student1.mul(student2, fill_value=0)
div = student1.div(student2, fill_value=0)

result = pd.DataFrame([add, sub, mul, div],
                      index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(result)

#        국어        수학    영어
# 덧셈   90.0   170.000  80.0
# 뺄셈  -90.0    10.000  80.0
# 곱셈    0.0  7200.000   0.0
# 나눗셈   0.0     1.125   inf