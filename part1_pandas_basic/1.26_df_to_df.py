# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:43:29 2023

@author: answl
"""

import pandas as pd
import seaborn as sns

# 타이타닉호 탑승자에 대한 인적사항(구조 여부 등)
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]

print(df.tail(), '\n')  # 마지막 5행만 표시
print(type(df), '\n')

add = df + 10
print(add.tail(), '\n')
print(type(add))

sub = add - df
print(sub.tail(), '\n')
print(type(sub))