# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:40:38 2023

@author: answl
"""

import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

# 0    2019-01-02
# 1          3.14
# 2           ABC
# 3           100
# 4          True
# dtype: object

idx = sr.index
val = sr.values

print(idx)  # RangeIndex(start=0, stop=5, step=1)
print('\n')
print(val)  # ['2019-01-02' 3.14 'ABC' 100 True]