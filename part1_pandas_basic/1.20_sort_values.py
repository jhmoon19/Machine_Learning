# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:12:01 2023

@author: answl
"""

import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# c1 열 기준으로 내림차순 정렬 
ndf = df.sort_values(by='c1', ascending = False)
print(ndf)

#     c0  c1  c2  c3  c4
# r2   3   6   9  12  15
# r1   2   5   8  11  14
# r0   1   4   7  10  13