# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:01:26 2023

@author: answl
"""

import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data)  

print(type(df))  # <class 'pandas.core.frame.DataFrame'>
print('\n')
print(df)

#    c0  c1  c2  c3  c4
# 0   1   4   7  10  13
# 1   2   5   8  11  14
# 2   3   6   9  12  15

print(df.index)     # RangeIndex(start=0, stop=3, step=1)
print(df.columns)   # Index(['c0', 'c1', 'c2', 'c3', 'c4'], dtype='object)