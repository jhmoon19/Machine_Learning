# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:52:54 2023

@author: answl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

''' STEP 1: 데이터 준비 '''

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

print(df.head())
print('\n')

# IPython 디스플레이 설정: 열 개수 한도 늘리기
pd.set_option('display.max_columns', 10)
print(df.head())


''' STEP 2: 데이터 탐색 '''

# 데이터 자료형 확인
print(df.info(), '\n')

# 데이터 통계 요약 정보 확인
print(df.describe())

### horsepower 열의 자료형 변경 (문자열>실수형)
print(df['horsepower'].unique(), '\n') # 고유값 확인(리스트)

# ?을 nan 으로 변경
df['horsepower'].replace('?', np.nan, inplace=True)
# 누락 데이터 행 삭제 (dropna)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
# 문자열을 실수형으로 
df['horsepower'] = df['horsepower'].astype('float')

print(df.describe())


''' STEP 3: 속성 선택 '''

ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]
print(ndf.head())

# 1. Matplotlib 산점도
ndf.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10,5))
plt.show()
plt.close()

# 2. seaborn regplot으로 산점도 그리기
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax1) # 회귀선 표시
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax2, fit_reg = False) # 회귀선 미표시
plt.show()
plt.close()

# 3. seaborn 조인트 그래프: 산점도&히스토그램
sns.jointplot(x='weight', y='mpg', data=ndf) # 회귀선 미표시
sns.jointplot(x='weight', y='mpg', kind='reg', data=ndf) # 회귀선 표시
plt.show()
plt.close()

# 4. seaborn pairplot: 두 변수 간 모두 경우의 수
grid_ndf = sns.pairplot(ndf)
plt.show()
plt.close()


''' STEP 4: 훈련/검증 데이터 분할 '''

# 속성 선택
x = ndf[['weight']] # 독립변수
y = ndf['mpg']      # 종속변수

# print(x, '\n')
# print(y)

# train data, test data 구분 (7:3)
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x,y,test_size=0.3, random_state=10)

print('train data 개수: ', len(x_train)) # 264
print('test data 개수: ', len(x_test))   # 118


''' STEP 5: 모형 학습 및 검증 '''

# sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.linear_model import LinearRegression

# 단순회귀분석 모형 객체 생성
lr = LinearRegression()

# train data로 모형 학습
lr.fit(x_train, y_train)

# 학습 마친 모형에 test data 적용하여 결정계수(R제곱) 계산
r_square = lr.score(x_test, y_test)
print(r_square) # 0.6822458558299325

'''결정계수 값 클수록 모형의 예측 능력이 좋다!'''

# 회귀선의 기울기
print('기울기 a: ', lr.coef_, '\n') # [-0.00775343]

# 회귀선의 y절편
print('y절편 b', lr.intercept_) # 6.710366257280086


# 모형에 전체 x 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교
y_hat = lr.predict(x)

plt.figure(figsize=(10,5))
ax1 = sns.distplot(y, hist=False, label="y")
ax2 = sns.distplot(y_hat, hist=False, label="y_hat", ax=ax1)
plt.show()
plt.close()

'''
lr 모형의 예측값 y_hat은 오른쪽으로 편중된 반면, 
실제 y값은 왼쪽으로 편향되어 있음.
--> 모형 오차 줄일 필요성 있음!
--> 비선형 회귀분석 필요! (곡선 선형 관계)
'''