# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:54:14 2023

@author: answl
"""

import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 행 인덱스 재설정: reindex([__, __, __])
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)
print('\n')

#      c0   c1   c2    c3    c4
# r0  1.0  4.0  7.0  10.0  13.0
# r1  2.0  5.0  8.0  11.0  14.0
# r2  3.0  6.0  9.0  12.0  15.0
# r3  NaN  NaN  NaN   NaN   NaN
# r4  NaN  NaN  NaN   NaN   NaN

# NaN : Not a Number (누락 데이터)

new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0) # 0으로 채우기
print(ndf2)
print('\n')

#     c0  c1  c2  c3  c4
# r0   1   4   7  10  13
# r1   2   5   8  11  14
# r2   3   6   9  12  15
# r3   0   0   0   0   0
# r4   0   0   0   0   0

# 행 하나만 단순히 추가하는 거라면
ndf2.loc['r5'] = 0
print(ndf2)
print('\n')

ndf2.loc['r6', 'r7'] = 0 
print(ndf2)

#      c0   c1   c2    c3    c4   r7
# r0  1.0  4.0  7.0  10.0  13.0  NaN
# r1  2.0  5.0  8.0  11.0  14.0  NaN
# r2  3.0  6.0  9.0  12.0  15.0  NaN
# r3  0.0  0.0  0.0   0.0   0.0  NaN
# r4  0.0  0.0  0.0   0.0   0.0  NaN
# r5  0.0  0.0  0.0   0.0   0.0  NaN
# r6  NaN  NaN  NaN   NaN   NaN  0.0