import pandas as pd  # 데이터 처리
import matplotlib.pyplot as plt  # 그래프 생성
import numpy as np  # 수치 계산
import folium  # 지도 시각화
import os  # 파일 시스템 조작(html)

class AirQualityAnalys:

    # 클래스 초기화
    def __init__(self):
        # Excel 파일에서 데이터 로드
        self.df = pd.read_excel("날짜별 미세먼지 수치.xlsx")  # 일별 미세먼지 데이터
        self.dfM = pd.read_excel("서울시 월별 평균 대기오염도 정보.xlsx")  # 월별 평균 데이터
        self.coord = pd.read_excel("서울시_자치구_중심점_2017.xlsx")  # 자치구별 좌표 데이터
        
        # 지도의 초기 중심점 설정 (첫 번째 자치구의 좌표 사용)
        self.latitude = self.coord['Y'].iloc[0]  # 위도
        self.longitude = self.coord['X'].iloc[0]  # 경도
        
    # 1번(미세먼지), 2번(초미세먼지) 주의구역 표시
    def display_map(self, map_type):
        # 초기 지도 생성
        mymap = folium.Map(location=[self.latitude, self.longitude], zoom_start=11)
        map = self.df.head(25)
            
        if map is not None:
            # 필터링된 데이터의 각 행에 대해 마커 생성
            for _, row in map.iterrows():
                region_name = row['측정소명']
                # 해당 지역의 좌표 찾기
                matchcoord = self.coord[self.coord['시군구명'] == region_name]
                
                if not matchcoord.empty:
                    # 마커 생성, 정보 추가
                    lat = matchcoord['Y'].values[0]
                    lon = matchcoord['X'].values[0]
                    if map_type == '1': # 미세먼지 map
                        if float(row['미세먼지(㎍/㎥)']) < 30:
                            folium.Marker([lat, lon], popup=f"{region_name}:\n 미세먼지 {row['미세먼지(㎍/㎥)']}㎍/㎥", icon=folium.Icon(icon="cloud", color="green")).add_to(mymap)
                        elif float(row['미세먼지(㎍/㎥)']) >= 30:
                            folium.Marker([lat, lon], popup=f"{region_name}:\n 미세먼지 {row['미세먼지(㎍/㎥)']}㎍/㎥", 
                                        icon=folium.Icon(icon="remove", prefix="glyphicon", color="red")).add_to(mymap)
                    if map_type == '2': # 초 미세먼지 map
                        if float(row['초미세먼지(㎍/㎥)']) < 25:
                            folium.Marker([lat, lon], popup=f"{region_name}:\n 초미세먼지 {row['초미세먼지(㎍/㎥)']}㎍/㎥", icon=folium.Icon(icon="cloud", color="green")).add_to(mymap)
                        elif float(row['초미세먼지(㎍/㎥)']) >= 25:
                            folium.Marker([lat, lon], popup=f"{region_name}:\n 초미세먼지 {row['초미세먼지(㎍/㎥)']}㎍/㎥", 
                                        icon=folium.Icon(icon="remove", prefix="glyphicon", color="red")).add_to(mymap)                                            
            
            # 생성된 지도를 HTML 파일로 저장, 브라우저에서 열기
            mymap.save('mymap.html')
            os.startfile('mymap.html')

    # 지역별 미세먼지 추이 그래프 구현
    def plot_region(self, region_name, graph_type):
        # 선택에 따라 데이터 결정
        if graph_type == '3':  # 날짜별 미세먼지 데이터 (최근 한달)
            data = self.df[self.df['측정소명'] == region_name].head(30).sort_values('측정일시', ascending=True) # 최근 한달 슬라이싱
            time_column = '측정일시'
            title_prefix = "최근 1개월"
        elif graph_type == '4':  # 월별 미세먼지 데이터 (최근 3년)
            data = self.dfM[self.dfM['측정소명'] == region_name].head(36).sort_values('측정월', ascending=True) # 최근 3년 슬라이싱
            time_column = '측정월'
            title_prefix = "최근 36개월"
        else:
            data = None
            
        if data is not None and not data.empty:
            # 그래프 스타일 설정
            ax = self.plot_style()
            
            # x축 눈금 간격 설정 
            x_nunguem = np.arange(len(data))
            tick_gangyeok = len(data) // 10
            selected_nunguem = x_nunguem[::tick_gangyeok]
            selected_labels = data[time_column].iloc[::tick_gangyeok]
                
            # 미세먼지 데이터 플롯
            ax.plot(x_nunguem, data['미세먼지(㎍/㎥)'], label='미세먼지(㎍/㎥)', color='dodgerblue', marker='^', markersize=8, linewidth=2)
            
            # 초미세먼지 데이터 플롯
            ax.plot(x_nunguem, data['초미세먼지(㎍/㎥)'], label='초미세먼지(㎍/㎥)', color='darkred', marker='o', markersize=8, linewidth=2)
            
            # 그래프 스타일
            ax.grid(axis='y', linestyle='--', alpha=0.7)  # y축 그리드 추가
            ax.set_xticks(selected_nunguem)  # x축 눈금 위치 설정
            ax.set_xticklabels(selected_labels, rotation=30, ha='right')  # x축 라벨 회전
            
            # 그래프 제목과 축 라벨 설정
            ax.set_title(
                f"{region_name} 자치구의 {title_prefix} 미세먼지 및 초미세먼지 추이",
                fontsize=16,
                fontweight='bold',
                color='darkblue'
            )
            ax.set_xlabel("시간", fontsize=14, color='darkgreen')
            ax.set_ylabel("㎍/㎥", fontsize=14, color='darkgreen')
            ax.legend(loc='upper left', fontsize=12, frameon=False)
            
            plt.show()  # 그래프 표시
        else:
            print(f"{region_name} 자치구의 데이터가 존재하지 않습니다.")

    # 그래프 설정 메서드
    def plot_style(self):
        plt.rc('font', family='Gulim')  # 한글 폰트 설정
        w, h = 12, 6  # 그래프 크기 설정
        margin = 0.5  # 여백 설정
        # 배경색이 있는 새 그래프 생성
        fig = plt.figure(figsize=(w, h), facecolor='lightblue')
        # 여백을 고려한 그래프 영역 설정
        ax = fig.add_axes([margin / w, margin / h, (w - 2 * margin) / w, (h - 2 * margin) / h])
        plt.style.use('ggplot')  # ggplot 스타일 적용
        return ax

analyzer = AirQualityAnalys()  # 분석 객체 생성
while True:
    # 사용자 메뉴 표시 및 입력 받기
    choice = input("1. 미세먼지 주의 구역 조회 2. 초미세먼지 주의 구역 조회 3. 날짜별 미세먼지 추이 조회 4. 월별 미세먼지 추이 조회 5. 종료: ")
    
    if choice in ['1', '2']:  # 미세먼지 지도
        analyzer.display_map(choice)
    elif choice in ['3', '4']:  # 추이 그래프
        region = input("조회하고 싶은 자치구 입력: ")
        analyzer.plot_region(region, choice)
    elif choice == '5':  # 프로그램 종료
        break
    else:  # 잘못된 입력 처리
        print("잘못된 입력입니다.")
