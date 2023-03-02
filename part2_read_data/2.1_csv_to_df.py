# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:58:24 2023

@author: answl
"""

import pandas as pd

file_path = './read_csv_sample.csv'

df1 = pd.read_csv(file_path)
print(df1, '\n')

#    c0  c1  c2  c3
# 0   0   1   4   7
# 1   1   2   5   8
# 2   2   3   6   9 

df2 = pd.read_csv(file_path, header=None)
print(df2, '\n')

#     0   1   2   3
# 0  c0  c1  c2  c3
# 1   0   1   4   7
# 2   1   2   5   8
# 3   2   3   6   9 

# header=None 설정하지 않으면 첫행(0행)이 헤더로 자동설정
df3 = pd.read_csv(file_path, index_col=None)
print(df3, '\n')

#    c0  c1  c2  c3
# 0   0   1   4   7
# 1   1   2   5   8
# 2   2   3   6   9 

df4 = pd.read_csv(file_path, index_col='c0')
print(df4)

#     c1  c2  c3
# c0            
# 0    1   4   7
# 1    2   5   8
# 2    3   6   9