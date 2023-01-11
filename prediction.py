# 패키지설치
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

#database의 파일 불러옴.
from database import a

#parameter 입력
while (True):
    try:
        print('지역 번호를 입력하세요.:')
        number=int(input())

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
        wd = input()
        wd_t = {'북북동': 22.5, '북동': 45, '동북동': 67.5, '동': 90, '동남동': 112.5, '남동': 135, '남남동': 157.5, '남': 180,
                '남남서': 202.5, '남서': 225, '서남서': 247.5, '서': 270, '서북서': 292.5, '북서': 315, '북북서': 337.5, '북': 360}
        wd_num = float((wd_t[wd]))

        print('하루 전의 산둥반도 초미세먼지 농도값을 입력하세요.')
        sdud = float(input())

        print('현재 초미세먼지 농도값을 입력하세요.')
        ud = float(input())
        break
    except ValueError:
        print('잘못된 값입니다.')
    except KeyError:
        print('잘못된 값입니다.')



test = pd.DataFrame([(rain, ws, wd_num, sdud, ud)])

data_m = a[number - 1].dropna()
data_X = data_m[data_m.columns[2:7]]
data_Y = data_m[data_m.columns[7:8]]
X_train, X_test, Y_train, Y_test = train_test_split(data_X, data_Y, test_size=0.2)

gdb = GradientBoostingRegressor(learning_rate=A, max_depth=B, n_estimators=C)
gdb.fit(X_train, Y_train.values.ravel())
gdb.pred = gdb.predict(test)



print('한 시간 뒤 초미세먼지 농도:', gdb.pred)