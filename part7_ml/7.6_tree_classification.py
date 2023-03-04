# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:31:29 2023

@author: answl
"""

import pandas as pd
import numpy as np

''' STEP 1: 데이터 준비 & 기본 설정 '''

# Breast Cancer 데이터셋 가져오기 
uci_path = "https://archive.ics.uci.edu/ml/machine-learning-databases/\
breast-cancer-wisconsin/breast-cancer-wisconsin.data"
df = pd.read_csv(uci_path, header=None)

df.columns = ['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
              'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses', 'class']

pd.set_option('display.max_columns', 15)


''' STEP 2: 데이터 탐색 '''

# 1. 데이터 어떻게 생겼는지 확인
print(df.head(), '\n')
#         id  clump  cell_size  cell_shape  adhesion  epithlial bare_nuclei  \
# 0  1000025      5          1           1         1          2           1   
# 1  1002945      5          4           4         5          7          10   
# 2  1015425      3          1           1         1          2           2   
# 3  1016277      6          8           8         1          3           4   
# 4  1017023      4          1           1         3          2           1   

#    chromatin  normal_nucleoli  mitoses  class  
# 0          3                1        1      2  
# 1          3                2        1      2  
# 2          3                1        1      2  
# 3          3                7        1      2  
# 4          3                1        1      2

# 2. 데이터 각 열의 자료형 확인 (+ NaN값 아닌 것의 개수)
print(df.info(), '\n')
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 699 entries, 0 to 698
# Data columns (total 11 columns):
#  #   Column           Non-Null Count  Dtype 
# ---  ------           --------------  ----- 
#  0   id               699 non-null    int64 
#  1   clump            699 non-null    int64 
#  2   cell_size        699 non-null    int64 
#  3   cell_shape       699 non-null    int64 
#  4   adhesion         699 non-null    int64 
#  5   epithlial        699 non-null    int64 
#  6   bare_nuclei      699 non-null    object
#  7   chromatin        699 non-null    int64 
#  8   normal_nucleoli  699 non-null    int64 
#  9   mitoses          699 non-null    int64 
#  10  class            699 non-null    int64 
# dtypes: int64(10), object(1)
# memory usage: 60.2+ KB
# None

# 3. 데이터 통계 요약 정보 확인 (개수, 평균, 표준편차, 최소값, 최대값, 4분위값)
print(df.describe(), '\n')
                 # id       clump   cell_size  cell_shape    adhesion  \
# count  6.990000e+02  699.000000  699.000000  699.000000  699.000000   
# mean   1.071704e+06    4.417740    3.134478    3.207439    2.806867   
# std    6.170957e+05    2.815741    3.051459    2.971913    2.855379   
# min    6.163400e+04    1.000000    1.000000    1.000000    1.000000   
# 25%    8.706885e+05    2.000000    1.000000    1.000000    1.000000   
# 50%    1.171710e+06    4.000000    1.000000    1.000000    1.000000   
# 75%    1.238298e+06    6.000000    5.000000    5.000000    4.000000   
# max    1.345435e+07   10.000000   10.000000   10.000000   10.000000   

#         epithlial   chromatin  normal_nucleoli     mitoses       class  
# count  699.000000  699.000000       699.000000  699.000000  699.000000  
# mean     3.216023    3.437768         2.866953    1.589413    2.689557  
# std      2.214300    2.438364         3.053634    1.715078    0.951273  
# min      1.000000    1.000000         1.000000    1.000000    2.000000  
# 25%      2.000000    2.000000         1.000000    1.000000    2.000000  
# 50%      2.000000    3.000000         1.000000    1.000000    2.000000  
# 75%      4.000000    5.000000         4.000000    1.000000    4.000000  
# max     10.000000   10.000000        10.000000   10.000000    4.000000

# bare_nuclei 열의 자료형 변경 (문자열-->숫자)
print(df['bare_nuclei'].unique(), '\n')
# ['1' '10' '2' '4' '3' '9' '7' '?' '5' '8' '6'] 
# '?'를 없애기 위해 1) nan으로 변경하고 2) dropna 3) 해당 열을 astype('int')
df['bare_nuclei'].replace('?', np.nan, inplace=True)
df.dropna(subset=['bare_nuclei'], axis=0, inplace=True)
df['bare_nuclei'] = df['bare_nuclei'].astype('int')

print(df.describe(), '\n')


''' STEP 3: 데이터셋 구분 '''

x = df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
              'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses']]
y = df['class']

from sklearn import preprocessing
x = preprocessing.StandardScaler().fit(x).transform(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=10)

print('train data 개수: ', x_train.shape)     # (478, 9)
print('test data 개수: ', x_test.shape)       # (205, 9)


''' STEP 4: Deicision Tree 분류 모형 : sklearn 사용 '''

from sklearn import tree

# 모형 객체 생성
tree_model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)

# 모형 학습
tree_model.fit(x_train, y_train)

# test_data로 y_hat 예측(분류)
y_hat = tree_model.predict(x_test)
# 2: benign(양성), 4: malignant(악성)

print(y_hat[0:10])                  # [4 4 4 4 4 4 2 2 4 4]
print(y_test.values[0:10], '\n')    # [4 4 4 4 4 4 2 2 4 4]

# 모형 성능 평가 
from sklearn import metrics

tree_matrix = metrics.confusion_matrix(y_test, y_hat)
print(tree_matrix, '\n')
# [[127   4]
#  [  2  72]] 

tree_report = metrics.classification_report(y_test, y_hat)
print(tree_report)
#               precision    recall  f1-score   support

#            2       0.98      0.97      0.98       131
#            4       0.95      0.97      0.96        74

#     accuracy                           0.97       205
#    macro avg       0.97      0.97      0.97       205
# weighted avg       0.97      0.97      0.97       205














