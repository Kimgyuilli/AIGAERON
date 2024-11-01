import pandas as pd
import folium
import tkinter as tk
from tkinter import Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os

location = input("찾을 지역을 입력하세요: ")
df=pd.read_excel('전국도시공원정보표준데이터.xlsx')
df = df.dropna(subset=['소재지지번주소', '위도', '경도'])
df=df.query("소재지지번주소.str.contains(@location)", engine='python')

# 지역의 첫 번째 위도와 경도를 사용하여 mymap을 초기화
latitude = df['위도'].iloc[0] if not df.empty else 33.371296
longitude = df['경도'].iloc[0] if not df.empty else 126.560056
mymap=folium.Map(location=[latitude, longitude], zoom_start=11)

for i in range(len(df)):
    folium.Marker([float(df['위도'][i:i+1]), float(df['경도'][i:i+1])],popup=df['공원명'][i:i+1]).add_to(mymap)

# HTML 파일로 저장
mymap.save('mymap.html')

# tkinter를 사용하여 GUI 창 생성
root = tk.Tk()
root.title("지도 보기")

# Frame 생성
frame = Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# HTML 파일을 tkinter에서 보여주기 위한 방법
def show_map():
    os.startfile('mymap.html')  # HTML 파일을 기본 브라우저로 열기

# 버튼 생성
button = os.startfile('mymap.html')  # HTML 파일을 기본 브라우저로 열기

root.mainloop()