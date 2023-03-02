# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:08:59 2023

@author: answl
"""

import pandas as pd

df = pd.read_json('./read_json_sample.json')
print(df, '\n')

#            name  year        developer opensource
# pandas           2008    Wes Mckinneye       True
# NumPy            2006  Travis Oliphant       True
# matplotlib       2003   John D. Hunter       True 

print(df.index)

# Index(['pandas', 'NumPy', 'matplotlib'], dtype='object')