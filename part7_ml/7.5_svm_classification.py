# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:09:58 2023

@author: answl
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

print(df.head(), '\n')

pd.set_option('display.max_columns', 15)
print(df.head(), '\n')


''' STEP 2: 데이터 탐색 & 전처리 '''

print(df.info())

# NaN 값 많은 deck 열 삭제
# embarked와 겹치는 embark_town 열 삭제
rdf = df.drop(['deck', 'embark_town'], axis=1)
print(rdf.columns.values)
# ['survived' 'pclass' 'sex' 'age' 'sibsp' 'parch' 'fare' 'embarked' 'class'
# 'who' 'adult_male' 'alive' 'alone']

# age 열 NaN 행 177개 삭제 
rdf = rdf.dropna(subset=['age'], how='any', axis=0)
print(len(rdf))  # 714

# embarked 열의 NaN 값을 최빈 승선도시 값으로 치환
most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
print(most_freq, '\n')  # S

print(rdf.describe(include='all'), '\n')

rdf['embarked'].fillna(most_freq, inplace=True)


''' STEP 3: 분석에 사용할 속성 선택 '''

ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head(), '\n')
#    survived  pclass     sex   age  sibsp  parch embarked
# 0         0       3    male  22.0      1      0        S
# 1         1       1  female  38.0      1      0        C
# 2         1       3  female  26.0      0      0        S
# 3         1       1  female  35.0      1      0        S
# 4         0       3    male  35.0      0      0        S

# 원핫인코딩: 범주형 데이터(sex, embarked)를 숫자형으로 변환 --> 모형이 인식 가능하도록
# = "더미 변수를 만든다" : 각각의 범주를 각각의 더미 변수 열로 만듦.
onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

# 열이름을 식별할 수 있도록 접두사 'town_'을 붙임. ex.town_C
onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_embarked], axis=1)

ndf.drop(['sex', 'embarked'], axis=1, inplace=True)
print(ndf.head(), '\n')
#    survived  pclass   age  sibsp  parch  female  male  town_C  town_Q  town_S
# 0         0       3  22.0      1      0       0     1       0       0       1
# 1         1       1  38.0      1      0       1     0       1       0       0
# 2         1       3  26.0      0      0       1     0       0       0       1
# 3         1       1  35.0      1      0       1     0       0       0       1
# 4         0       3  35.0      0      0       0     1       0       0       1


''' STEP 4: 데이터셋 구분 - 훈련 / 검증 데이터 '''

# 속성(변수, feature) 선택
x = ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male',
         'town_C', 'town_Q', 'town_S']]     # 독립 변수 (설명 변수)
y = ndf['survived']                         # 종속 변수 (예측 변수)

# 독립 변수 데이터를 정규화 (상대적 크기 차이 없애기 위함)
from sklearn import preprocessing
x = preprocessing.StandardScaler().fit(x).transform(x)

# 훈련 데이터, 검증 데이터 구분 (7:3)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=(10))

print('train data 개수: ', x_train.shape)  # (499, 9)
print('test data 개수: ', x_test.shape, '\n')    # (215, 9)


''' STEP 5: SVM 분류 모형 - sklearn 사용 '''

# SVM : Support Vector Machine
from sklearn import svm

# 모형 객체 생성
svm_model = svm.SVC(kernel='rbf')
# RBF : Radial Basis Function (방사형 기반 함수)
# 이외의 커널 : Linear, Polynimial, Sigmoid 등

# 학습 데이터로 모형 학습
svm_model.fit(x_train, y_train)

# 검증 데이터로 y_hat 예측 (분류)
y_hat = svm_model.predict(x_test)

print(y_hat[0:10])                  # [0 0 1 0 0 0 1 0 0 0]
print(y_test.values[0:10], '\n')    # [0 0 1 0 0 1 1 1 0 0] 

# 모형 성능 평가 1 : Confusion Matrix 계산
from sklearn import metrics
svm_matrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_matrix, '\n')
# [[120   5]     [[TP FP]  [[True Pos  / False Pos]
#  [ 35  55]]    [FN TN]]  [False Neg / True Neg]]

# 모형 성능 평가 2 : 평가 지표 계산
svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)
#               precision    recall  f1-score   support

#            0       0.77      0.96      0.86       125
#            1       0.92      0.61      0.73        90

#     accuracy                           0.81       215
#    macro avg       0.85      0.79      0.80       215
# weighted avg       0.83      0.81      0.81       215

# 생존자 예측의 정확도 : 65 / (15+65)  =  TN / FP+TN
# 생존자 예측의 재현률 : 65 / (65+25)  =  TN / FN+TN

'''
Q. f1-score = 정확도와 재현률의 평균?
A. 정확도와 재현률의 "조화평균" !
공식 : 2 * (precision * recall) / (precision + recall)
조화평균을 이용하면 산술평균을 이용하는 것보다, 큰 비중이 끼치는 bias가 줄어든다
'''