# python Terminal에다가 conda install -c conda-forge folium을 먼저 입력하고 난 뒤에 folium 패키지 사용이 사용가능합니다.
# 패키지 설치
import folium
import numpy as np
import pandas as pd


map_osm=folium.Map(location=[37.4483454,126.694595],zoom_start=10)
# openstreetmap을 이용합니다. location은 화면중앙 좌표, zoom_start는 지도 축척과 관련된 값입니다.


# 국가배경농도 측정망(국가배경농도 파악 및 외국유입/유출 파악) : 빨간색 마커로 표시.
folium.Marker(
  location=[37.964738,124.634011],
  popup='백령도 관측점',
  icon=folium.Icon(color='red',icon='star')
).add_to(map_osm)

# 교외대기 측정망(도시를 둘러싼 교외 지역의 배경농도 측정) : 초록색 마커로 표시.
folium.Marker(
  location=[37.233041,126.149283],
  popup='덕적도 관측점',
  icon=folium.Icon(color='green',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.710051, 126.271619],
  popup='석모리 관측점',
  icon=folium.Icon(color='green',icon='star')
).add_to(map_osm)

# 도시대기 측정망(도시를 둘러싼 교외 지역의 배경농도 측정) : 검은색 마커로 표시.
folium.Marker(
  location=[37.602125, 126.661277],
  popup='검단 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.545997, 126.730061],
  popup='계산 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.409124, 126.699817],
  popup='고잔 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.640861, 126.490987],
  popup='길상 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.403472, 126.727210],
  popup='논현 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.409468, 126.678282],
  popup='동춘 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.499703, 126.723768],
  popup='부평 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.513137, 126.736272],
  popup='삼산 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.502646, 126.674612],
  popup='석남 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.382130, 126.654754],
  popup='송도 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.473815, 126.643195],
  popup='송림 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.764529, 126.463920],
  popup='송해 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.459400, 126.657249],
  popup='숭의 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.468018, 126.635040],
  popup='신흥 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.541600, 126.681218],
  popup='연희 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.256002, 126.483283],
  popup='영흥 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.495599, 126.488692],
  popup='운서 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.594362, 126.698586],
  popup='원당 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.528196, 126.634897],
  popup='청라 관측점',
  icon=folium.Icon(color='black',icon='star')
).add_to(map_osm)


# 도로변대기 측정망(도시를 둘러싼 교외 지역의 배경농도 측정) : 파란색 마커로 표시.
folium.Marker(
  location=[37.442172,126.707263],
  popup='남동 관측점',
  icon=folium.Icon(color='blue',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.491098, 126.723769],
  popup='부평역 관측점',
  icon=folium.Icon(color='blue',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.457983, 126.691088],
  popup='석바위 관측점',
  icon=folium.Icon(color='blue',icon='star')
).add_to(map_osm)

folium.Marker(
  location=[37.482121, 126.636983],
  popup='송현 관측점',
  icon=folium.Icon(color='blue',icon='star')
).add_to(map_osm)

map_osm.save('Incheon_map.html')
# 저장된 프로젝트 폴더에 지도를 저장합니다.