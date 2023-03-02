# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:58:31 2023

@author: answl
"""

import pandas as pd

exam_data = {'이름':['서준', '우현', '인아'],
             '수학':[90,80,70],
             '영어':[98,89,95],
             '음악':[85,95,100],
             '체육':[100,90,90]}

df = pd.DataFrame(exam_data)

df.set_index('이름', inplace = True)
print(df)
print('\n')

# 전치1: 메소드 활용
df = df.transpose()
print(df)
print('\n')

# 이름   서준  우현   인아
# 수학   90  80   70
# 영어   98  89   95
# 음악   85  95  100
# 체육  100  90   90

# 전치2: 클래스 속성 활용
df = df.T
print(df)

#     수학  영어   음악   체육
# 이름                  
# 서준  90  98   85  100
# 우현  80  89   95   90
# 인아  70  95  100   90