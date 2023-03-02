# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:02:53 2023

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
print(type(df))
print('\n')

match1= df['수학']
print(match1)
print(type(match1)) # Series 타입
print('\n')

english = df.영어
print(english)
print(type(english)) # Series 타입

music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')

math2 = df[['수학']]
print(math2)
print(type(math2)) # DataFrame 타입