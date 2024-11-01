import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 엑셀 파일 읽기
df = pd.read_excel('주민등록인구.xlsx', thousands=',')

# 사용자 입력으로 두 개의 동명 가져오기
q1 = input("첫 번째 동명을 적으세요: ")
q2 = input("두 번째 동명을 적으세요: ")

# 입력된 동명으로 데이터 필터링
df1 = df.query('행정기관.str.contains("' + q1 + '")', engine='python')
df2 = df.query('행정기관.str.contains("' + q2 + '")', engine='python')

# 필요한 열만 선택
df1 = df1.iloc[:, 4:15]
df2 = df2.iloc[:, 4:15]

# 데이터를 numpy 배열로 변환하고 1차원으로 평탄화
arr1 = np.array(df1, dtype=int).flatten()
arr2 = np.array(df2, dtype=int).flatten()

# x축에 사용할 열 이름을 numpy 배열로 변환
df_x = np.array(df1.columns)

# 그래프 설정
plt.rc('font', family='Gulim')
plt.figure(figsize=(10, 7))
plt.title(q1 + "와 " + q2 + "의 인구 그래프")
plt.plot(df_x, arr1, marker='*', label=q1)
plt.plot(df_x, arr2, marker='o', label=q2)

plt.legend()  # 범례 추가
plt.show()