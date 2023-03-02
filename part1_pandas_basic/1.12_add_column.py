# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:39:52 2023

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

# '국어' 열 추가 
df['국어'] = 80 # 모든 행 값이 80으로 설정됨. [80, 80, 80]
print(df)

#    이름  수학  영어   음악   체육  국어
# 0  서준  90  98   85  100  80
# 1  우현  80  89   95   90  80
# 2  인아  70  95  100   90  80