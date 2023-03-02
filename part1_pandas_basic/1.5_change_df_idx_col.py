# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:12:03 2023

@author: answl
"""

import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index = ['준서', '예은'],
                  columns = ['나이', '성별', '학교'])

# 딕셔너리와 달리 리스트는 행이 된다.

#     나이 성별   학교
# 준서  15  남  덕영중
# 예은  17  여  수리중

print(df)
print('\n')
print(df.index)    # Index(['준서', '예은'], dtype='object')
print('\n')
print(df.columns)  # Index(['나이', '성별', '학교'], dtype='object')

# index와 columns 명 변경 가능!
df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']

print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)

#      연령 남녀   소속
# 학생1  15  남  덕영중
# 학생2  17  여  수리중