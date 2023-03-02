# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:19:59 2023

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

#    이름  수학  영어   음악   체육
# 0  서준  90  98   85  100
# 1  우현  80  89   95   90
# 2  인아  70  95  100   90

df.set_index('이름', inplace=True) # 행 이름으로 설정
print(df)

#     수학  영어   음악   체육
# 이름                  
# 서준  90  98   85  100
# 우현  80  89   95   90
# 인아  70  95  100   90

# 원소 1개 선택: '서준'의 '음악' 점수 --> 2가지 방법
a = df.loc['서준', '음악']
print(a)  # 85
b = df.iloc[0,2] # iloc[[0,2]]와 다름!
print(b)  # 85

# 원소 2개 선택: '서준'의 음악&체육 점수 --> 4가지 방법
c = df.loc['서준', ['음악', '체육']]
print(c)
d = df.iloc[0, [2,3]]
print(d)
e = df.loc['서준', '음악':'체육']
print(e)
f = df.iloc[0, 2:]
print(f)

# 원소 2개 선택: '서준'의 음악&체육 점수 --> 4가지 방법
g = df.loc[['서준', '우현'], ['음악', '체육']]
print(g)
h = df.iloc[[0,1], [2,3]]
print(h)
i = df.loc['서준':'우현', '음악':'체육']
print(i)
j = df.iloc[0:2, 2:]
print(j)

# 모든 행에 대한 2개 열
k = df.iloc[:, 2:]
print(k)
l = df.iloc[:, [2,3]]
print(l)