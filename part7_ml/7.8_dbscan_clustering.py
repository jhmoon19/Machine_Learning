# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 15:48:15 2023

@author: answl
"""

import pandas as pd
import folium

# 서울 시내 중학교 진학률 데이터셋
file_path = "./2016_middle_school_graduates_report.xlsx"
df = pd.read_excel(file_path, index_col=0)

pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

print(df.columns.values)
# [지역' '학교명' '코드' '유형' '주야' '남학생수' '여학생수'
# '일반고' '특성화고' '과학고' '외고_국제고' '예고_체고' '마이스터고' 
# '자사고' '자공고' '기타진학' '취업' '미상' '위도' '경도']


''' STEP 2: 데이터 탐색 '''

# 1. 데이터 어떻게 생겼는지 확인
print(df.head(), '\n')
#      지역                               학교명  코드  유형  주야  ...  \
# 0  성북구  서울대학교사범대학부설중학교.....       3  국립  주간  ...   
# 1  종로구  서울대학교사범대학부설여자중학교...     3  국립  주간  ...   
# 2  강남구           개원중학교                     3  공립  주간  ...   
# 3  강남구           개포중학교                     3  공립  주간  ...   
# 4  서초구           경원중학교                     3  공립  주간  ...   

#    기타진학  취업   미상       위도        경도  
# 0     0.004     0  0.000  37.594942  127.038909  
# 1     0.031     0  0.000  37.577473  127.003857  
# 2     0.009     0  0.003  37.491637  127.071744  
# 3     0.019     0  0.000  37.480439  127.062201  
# 4     0.010     0  0.000  37.510750  127.008900 

# 2. 데이터 각 열의 자료형 확인 (+ NaN값 아닌 것의 개수)
print(df.info(), '\n')
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 415 entries, 0 to 414
# Data columns (total 20 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   지역      415 non-null    object 
#  1   학교명     415 non-null    object 
#  2   코드      415 non-null    int64  
#  3   유형      415 non-null    object 
#  4   주야      415 non-null    object 
#  5   남학생수    415 non-null    int64  
#  6   여학생수    415 non-null    int64  
#  7   일반고     415 non-null    float64
#  8   특성화고    415 non-null    float64
#  9   과학고     415 non-null    float64
#  10  외고_국제고  415 non-null    float64
#  11  예고_체고   415 non-null    float64
#  12  마이스터고   415 non-null    float64
#  13  자사고     415 non-null    float64
#  14  자공고     415 non-null    float64
#  15  기타진학    415 non-null    float64
#  16  취업      415 non-null    int64  
#  17  미상      415 non-null    float64
#  18  위도      415 non-null    float64
#  19  경도      415 non-null    float64
# dtypes: float64(12), int64(4), object(4)
# memory usage: 68.1+ KB
# None 

# 3. 데이터 통계 요약 정보 확인 (개수, 평균, 표준편차, 최소값, 최대값, 4분위값)
print(df.describe(), '\n')
#              코드    남학생수    여학생수      일반고    특성화고  ...  \
# count  415.000000  415.000000  415.000000  415.000000  415.000000  ...   
# mean     3.197590  126.532530  116.173494    0.623080    0.149684  ...   
# std      0.804272   79.217906   76.833082    0.211093    0.102977  ...   
# min      3.000000    0.000000    0.000000    0.000000    0.000000  ...   
# 25%      3.000000   80.000000   71.500000    0.566500    0.065500  ...   
# 50%      3.000000  129.000000  118.000000    0.681000    0.149000  ...   
# 75%      3.000000  177.500000  161.500000    0.758000    0.224500  ...   
# max      9.000000  337.000000  422.000000    0.908000    0.477000  ...   

#          기타진학   취업        미상        위도        경도  
# count  415.000000  415.0  415.000000  415.000000  415.000000  
# mean     0.069571    0.0    0.001670   37.491969  127.032792  
# std      0.235630    0.0    0.003697    0.348926    0.265245  
# min      0.000000    0.0    0.000000   34.979940  126.639561  
# 25%      0.000000    0.0    0.000000   37.501934  126.921758  
# 50%      0.007000    0.0    0.000000   37.547702  127.013579  
# 75%      0.015000    0.0    0.003000   37.590670  127.071265  
# max      1.000000    0.0    0.036000   37.694777  129.106974 


# 지도에 위치 표시
mschool_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain',
                         zoom_start=12)

# 중학교 위치를 CircleMarker로 표시
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat, lng],
                        radius=5,
                        color='brown',
                        fill=True,
                        fill_color='coral',
                        fill_opacity=0.7,
                        popup=name).add_to(mschool_map)

# 지도를 html 파일로 저장
mschool_map.save('./seoul_mschool_location.html')


''' STEP 3: 데이터 전처리 '''

# 원핫인코딩 --> 더미 변수
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()

onehot_location = label_encoder.fit_transform(df['지역'])
onehot_code = label_encoder.fit_transform(df['코드'])
onehot_type = label_encoder.fit_transform(df['유형'])
onehot_day = label_encoder.fit_transform(df['주야'])

df['location'] = onehot_location
df['code'] = onehot_code
df['type'] = onehot_type
df['day'] = onehot_day

print(df.head(), '\n')
#      지역                               학교명  코드  유형  주야  ...  \
# 0  성북구  서울대학교사범대학부설중학교.....       3  국립  주간  ...   
# 1  종로구  서울대학교사범대학부설여자중학교...     3  국립  주간  ...   
# 2  강남구           개원중학교                     3  공립  주간  ...   
# 3  강남구           개포중학교                     3  공립  주간  ...   
# 4  서초구           경원중학교                     3  공립  주간  ...   

#          경도  location  code  type  day  
# 0  127.038909        16     0     1    0  
# 1  127.003857        22     0     1    0  
# 2  127.071744         0     0     0    0  
# 3  127.062201         0     0     0    0  
# 4  127.008900        14     0     0    0  

# [5 rows x 24 columns]


''' STEP 4: DBSCAN 군집 모형 - sklearn 사용 '''

# DBSCAN : Density-Based Spatial Clustering of Applications with Noise
# 뜻 : 공간밀집도 기준 군집화 
# - 반지름 R (eps), 공간 속 최소 포인트 개수 M (min_samples) 주어짐.
# - core point: 군집의 중심
# - border point: 군집 속 중심 외의 점들
# - Noise: 그 어디에도 속하지 않는 outlier

from sklearn import cluster

''' 1. 설명 변수: 과학고, 외고_국제고, 자사고 '''

columns_list = [9,10,13]
x = df.iloc[:, columns_list]
print(x[:5], '\n')

x = preprocessing.StandardScaler().fit(x).transform(x)

dbm = cluster.DBSCAN(eps=0.2, min_samples=5)

dbm.fit(x)

cluster_label = dbm.labels_
print(cluster_label, '\n')
# 군집은 -1(Noise)를 제외한 4개(0,1,2,3)

df['Cluster'] = cluster_label
print(df.head(), '\n')


# 클러스터 값으로 그룹화, 그룹별 내용 출력
grouped_cols = [0,1,3] + columns_list  # 지역,학교명,유형,과고/외고/자사고
grouped = df.groupby('Cluster')  # 판다스 메소드 groupby

# print(grouped)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002A8F85B7C70>
# print(list(grouped), '\n')  # [(-1, 해당 데이터), (0, 해당 데이터) ...]

for key, group in grouped:
    print('* key : ', key)              # 군집 번호 (-1,0,1,2,3)
    print('* number : ', len(group))    # 해당 군집에 속하는 학교 수
    print(group.iloc[:, grouped_cols].head())
    print('\n')
    
# 시각화
colors = {-1:'gray', 0:'coral', 1:'blue', 2:'green', 3:'red', 4:'purple', 
          5:'orange', 6:'brown', 7:'brick', 8:'yellow', 9:'magenta', 10:'cyan'}

cluster_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', 
                         zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster):
    folium.CircleMarker([lat, lng],
                        radius=5,
                        color=colors[clus],
                        fill=True,
                        fill_color=colors[clus],
                        fill_opacity=0.7,
                        popup=name).add_to(cluster_map)
    
cluster_map.save('./seoul_mschool_cluster.html')

''' 
<결과>
1) Noise 개수 : 255
2) 4개의 클러스터로 구분
'''


''' 2. 설명 변수: 과학고, 외고_국제고, 자사고 진학률 + 유형 '''

columns_list2 = [9,10,13,22]
x2 = df.iloc[:, columns_list2]
print(x2[:5], '\n')

x2 = preprocessing.StandardScaler().fit(x2).transform(x2)
dbm2 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm2.fit(x2)
df['Cluster2'] = dbm2.labels_


# 클러스터 값으로 그룹화, 그룹별 내용 출력
grouped2_cols = [0,1,3] + columns_list2  # 지역,학교명,유형,과고/외고/자사고
grouped2 = df.groupby('Cluster2')  # 판다스 메소드 groupby

# print(grouped)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002A8F85B7C70>
# print(list(grouped), '\n')  # [(-1, 해당 데이터), (0, 해당 데이터) ...]

for key, group in grouped2:
    print('* key : ', key)              # 군집 번호 (-1,0,1,2,3)
    print('* number : ', len(group))    # 해당 군집에 속하는 학교 수
    print(group.iloc[:, grouped2_cols].head())
    print('\n')

cluster2_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', 
                         zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster2):
    folium.CircleMarker([lat, lng],
                        radius=5,
                        color=colors[clus],
                        fill=True,
                        fill_color=colors[clus],
                        fill_opacity=0.7,
                        popup=name).add_to(cluster2_map)
    
cluster2_map.save('./seoul_mschool_cluster2.html')

''' 
<결과>
1) Noise 개수가 281개로 늘어남. (<--255)
2) 11개의 클러스터로 구분 (0~10)
'''


''' 3. 설명 변수: 과학고, 외고_국제고 '''

columns_list3 = [9,10]
x3 = df.iloc[:, columns_list3]
print(x3[:5], '\n')

x3 = preprocessing.StandardScaler().fit(x3).transform(x3)
dbm3 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm3.fit(x3)
df['Cluster3'] = dbm3.labels_


# 클러스터 값으로 그룹화, 그룹별 내용 출력
grouped3_cols = [0,1,3] + columns_list3  # 지역,학교명,유형,과고/외고/자사고
grouped3 = df.groupby('Cluster3')  # 판다스 메소드 groupby

# print(grouped)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002A8F85B7C70>
# print(list(grouped), '\n')  # [(-1, 해당 데이터), (0, 해당 데이터) ...]

for key, group in grouped3:
    print('* key : ', key)              # 군집 번호 (-1,0,1,2,3)
    print('* number : ', len(group))    # 해당 군집에 속하는 학교 수
    print(group.iloc[:, grouped3_cols].head())
    print('\n')

cluster3_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', 
                         zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster3):
    folium.CircleMarker([lat, lng],
                        radius=5,
                        color=colors[clus],
                        fill=True,
                        fill_color=colors[clus],
                        fill_opacity=0.7,
                        popup=name).add_to(cluster3_map)
    
cluster3_map.save('./seoul_mschool_cluster3.html')

''' 
<결과>
1) Noise 개수가 61개로 줄어듦. (<--281<--255)
2) 7개의 클러스터로 구분 (0~6)
'''


'''
<정리>
1) 속성 (설명 변수) 늘어남에 따라 
    군집에 속하지 못하는 Noise (outlier) 도 늘어나는 경향
2) 속성 늘어날수록 군집 개수도 늘어남. (아닐수도 있음.)
3) 필요성 : 적절한 R과 M값을 설정하기
'''














