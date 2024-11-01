import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel('성별_인구수.xlsx')
plt.rc('font',family='Gulim')
plt.title('총인구')
plt.plot(df['시점'],df['남자인구수'])
plt.plot(df['시점'],df['여자인구수'])
plt.show()