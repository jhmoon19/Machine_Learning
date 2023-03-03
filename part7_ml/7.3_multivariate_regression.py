# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:38:47 2023

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

x = ndf[['cylinders', 'horsepower', 'weight']] # 다중 독립변수
y = ndf['mpg']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state = 10)

print('훈련 데이터: ', x_train.shape) # (274, 3)
print('검증 데이터: ', x_test.shape)  # (118, 3)


from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x_train, y_train)

r_square = lr.score(x_test, y_test)
print(r_square, '\n') # 0.6939048496695599

print('x 변수의 계수 a: ', lr.coef_, '\n') # [-0.60691288 -0.03714088 -0.00522268]

print('상수항 b', lr.intercept_)  # 46.414351269634004


''' 학습 데이터 산점도와 검증 데이터로 예측한 회귀선 '''

y_hat = lr.predict(x_test)

plt.figure(figsize=(10,5))
ax1 = sns.distplot(y_test, hist=False, label="y_test")
ax2 = sns.distplot(y_hat, hist=False, label="y_hat", ax=ax1)
plt.show()
plt.close()