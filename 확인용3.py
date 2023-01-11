from sklearn.ensemble import GradientBoostingRegressor
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


a1=pd.read_excel('백령도 20182020.xlsx')
a2=pd.read_excel('검단 20182020.xlsx')
a=[a1,a2]


print('예측 지역 번호를 입력하세요. (1:백령도, 2:검단, 3:, 4:, 5:, 6:,7:,8:,9:,10:,11:) :')
x=int(input())

if 0<x<29:
     data_m=a[x-1].dropna()
     data_X = data_m[data_m.columns[1:6]]
     data_Y = data_m[data_m.columns[6:7]]
     X_train, X_test, Y_train, Y_test = train_test_split(data_X, data_Y, test_size=0.2)
     LR = {'learning_rate': [0.0001, 0.0005, 0.001, 0.005, 0.01], 'n_estimators': [100, 200, 300, 400, 500],'max_depth': [2, 3, 4, 5, 6]}
     tuning = GridSearchCV(estimator=GradientBoostingRegressor(), param_grid=LR, scoring='r2')
     tuning.fit(X_train, Y_train.values.ravel())
     print(tuning.best_params_, tuning.best_score_)

     print('learning_rate 값을 입력하세요.:')
     A = float(input())

     print('max_depth 값을 입력하세요:')
     B = int(input())

     print('n_estimators 값을 입력하세요:')
     C = int(input())

     print('강수량을 입력하세요.')
     rain = float(input())

     print('풍속을 입력하세요.')
     ws = float(input())

     print('풍향을 입력하세요.')
     wd = float(input())

     print('하루 전의 산둥반도 초미세먼지 농도값을 입력하세요.')
     sdud = float(input())

     print('현재 초미세먼지 농도값을 입력하세요.')
     ud = float(input())

     test=pd.DataFrame([(rain,ws,wd,sdud,ud)])

     gdb = GradientBoostingRegressor(learning_rate=A, max_depth=B, n_estimators=C)
     gdb.fit(X_train, Y_train.values.ravel())
     gdb.pred = gdb.predict(test)
     print('한 시간 뒤 초미세먼지 농도:', gdb.pred)

else:
     print('유효하지 않은 번호입니다.')


