# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:49:22 2023

@author: answl
"""

import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
print(sr)

# 이름              영인
# 생년월일    2010-05-01
# 성별               여
# 학생여부          True
# dtype: object

print(sr[0])
print(sr['이름'])

print(sr[[1,2]])  # 성별 포함
print('\n')
print(sr[['생년월일', '성별']])

print(sr[1:2])  # 성별 불포함
print('\n')
print(sr['생년월일':'성별']) # 성별 포함