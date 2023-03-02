# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:23:23 2023

@author: answl
"""

import pandas as pd

dict_data = {'a':1, 'b':2, 'c':3}

sr = pd.Series(dict_data)

print(type(sr)) # <class 'pandas.core.series.Series'>
print('\n')
print(sr)

# a    1
# b    2
# c    3
# dtype: int64

print(sr.index)     # Index(['a','b','c'], dtype='object')
print(sr.values)    # array([1.52, 2.3, 3.01])