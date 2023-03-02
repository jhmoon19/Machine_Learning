# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:42:48 2023

@author: answl
"""

import pandas as pd

exam_data = {'이름':['서준', '우현', '인아'],
             '수학':[90,80,70],
             '영어':[98,89,95],
             '음악':[85,95,100],
             '체육':[100,90,90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 3 인덱스 행 추가 (모든 값 0)
df.loc[3] = 0
print(df)
print('\n')

df.loc[4] = ['동규', 90, 80, 70, 60]
print(df)
print('\n')

# 행이름 바꿔서 & 3인덱스 행 값 복사
df.loc['행5'] = df.loc[3]
print(df)