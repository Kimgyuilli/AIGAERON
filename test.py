import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 타이타닉 데이터셋 로드
titanic = sns.load_dataset('titanic')

# 동반한 형제 자매 및 배우자 수에 따른 생존율 계산
survival_rate = titanic.groupby('sibsp')['survived'].mean().reset_index()

# 생존율 출력
print(survival_rate)

survival_rate2 = titanic.groupby('parch')['survived'].mean().reset_index()

# 생존율 출력
print(survival_rate2)
survival_rate3 = titanic.groupby('alone')['survived'].mean().reset_index()

# 생존율 출력
print(survival_rate3)
