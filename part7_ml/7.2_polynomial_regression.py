# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 08:43:22 2023

@author: answl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]

x = ndf[['weight']]
y = ndf['mpg']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state = 10)

print('훈련 데이터: ', x_train.shape, len(x_train)) # (274, 1) 274
print('검증 데이터: ', x_test.shape, len(x_test))  # (118, 1) 118


''' 비선형회귀분석 모형 - sklearn 사용 '''

from sklearn.linear_model import LinearRegression     # 선형회귀분석
from sklearn.preprocessing import PolynomialFeatures  # 다항식 변환

poly = PolynomialFeatures(degree=2)         # 2차항 객체 만들기
x_train_poly = poly.fit_transform(x_train)  # x_train 데이터를 2차항으로 변경

print('원 데이터: ', x_train.shape)                 # (274, 1)
print('2차항 변환 데이터: ', x_train_poly.shape)     # (274, 3)
# 1개였던 열이 2차항 데이터에서는 3개로 늘어난 모습 

print(x_train, '\n')
#      weight
# 38   4209.0
# 172  2223.0
# 277  3410.0
# 196  2164.0
# 357  2615.0 ...
print(x_train_poly,'\n')
# [[1.0000000e+00 4.2090000e+03 1.7715681e+07]
#  [1.0000000e+00 2.2230000e+03 4.9417290e+06]
#  [1.0000000e+00 3.4100000e+03 1.1628100e+07]
#  [1.0000000e+00 2.1640000e+03 4.6828960e+06]
#  [1.0000000e+00 2.6150000e+03 6.8382250e+06]...]


# 2차항 독립변수로 모형 학습
pr = LinearRegression()
pr.fit(x_train_poly, y_train)

# 학습 마친 모형에 test_data로 결정계수(R제곱) 계산
x_test_poly = poly.fit_transform(x_test) # x_test 데이터도 2차항 변형
r_square = pr.score(x_test_poly, y_test)
print(r_square)  # 0.7087009262975685


''' 훈련 데이터 산점도 vs test data로 예측한 회귀선 '''

# 2차항 변형된 검증 데이터를 모형으로 예측한 결과: y_hat_test
y_hat_test = pr.predict(x_test_poly)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.plot(x_train, y_train, 'o', label = 'Train Data')
ax.plot(x_test, y_hat_test, 'r+', label = 'Predicted Value')
ax.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()
plt.close()


''' 전체 x 데이터 2차항 변경 후 예측한 값 y_hat vs 실제 y값 '''

x_ploy = poly.fit_transform(x)
y_hat = pr.predict(x_ploy)

plt.figure(figsize=(10,5))
ax1 = sns.distplot(y, hist = False, label='y')
ax1 = sns.distplot(y_hat, hist = False, label='y_hat', ax=ax1)
plt.show()
plt.close()




