# 패키지설치
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

#  다 모아둔 excel 파일이 데이터베이스파일에 모듈형태로 저장됨. 이를 불러옴.
from database import a

print('예측 지역 번호를 정확히 입력하세요. (1:검단, 2:계산, 3:고잔, 4:구월, 5:길상,6:남동,7:논현,8:덕적도,9:동춘,10:백령도,11:부평')
print('12:부평역,13:삼산,14:석모리,15:석바위,16:송도,17:송림,18:송해,19:송현,20:숭의,21:신흥,22:연희,23:영흥,24:운서,25:원당,26:청라)')
x=int(input())

if 0<x<26:
     data_m=a[x-1].dropna()
     data_X = data_m[data_m.columns[1:6]]
     data_Y = data_m[data_m.columns[6:7]]
     X_train, X_test, Y_train, Y_test = train_test_split(data_X, data_Y, test_size=0.2)
     LR = {'learning_rate': [0.001, 0.005, 0.01], 'n_estimators': [100, 200, 300, 400, 500],'max_depth': [2,3,4,5,6]}
     tuning = GridSearchCV(estimator=GradientBoostingRegressor(), param_grid=LR, scoring='r2')
     tuning.fit(X_train, Y_train.values.ravel())
     print(tuning.best_params_, tuning.best_score_)

     print('예측에 필요한 최적의 learning_rate, n_estimators, max_depth를 구했습니다.')

else:
    print('유효하지 않은 번호입니다.')