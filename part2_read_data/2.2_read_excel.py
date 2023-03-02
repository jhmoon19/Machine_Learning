# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:04:56 2023

@author: answl
"""

import pandas as pd 

df1 = pd.read_excel('./남북한발전전력량.xlsx')
df2 = pd.read_excel('./남북한발전전력량.xlsx', header = None)

print(df1, '\n')
print(df2)