# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:13:05 2023

@author: answl
"""

import pandas as pd

url = './sample.html'

tables = pd.read_html(url)
print(tables, '\n')
# [   Unnamed: 0  c0  c1  c2  c3
# 0           0   0   1   4   7
# 1           1   1   2   5   8
# 2           2   2   3   6   9,          name  year        developer  opensource
# 0       NumPy  2006  Travis Oliphant        True
# 1  matplotlib  2003   John D. Hunter        True
# 2      pandas  2008    Wes Mckinneye        True] 

print(len(tables), '\n')

for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print('\n')
    
df = tables[1]

df.set_index(['name'], inplace = True)
print(df)

#             year        developer  opensource
# name                                         
# NumPy       2006  Travis Oliphant        True
# matplotlib  2003   John D. Hunter        True
# pandas      2008    Wes Mckinneye        True