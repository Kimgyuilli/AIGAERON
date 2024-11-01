import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

tip_data = sns.load_dataset('tips')
print(tip_data)

# df = tip_data.select_dtypes(include=[np.number]).corr()
# # sns.pairplot(data = tip_data, hue = 'time')
# # sns.regplot(data = tip_data, x = 'total_bill', y='tip')
# sns.heatmap(data = df, annot=True, fmt='.2f', cbar=False)
plt.title(":(")
plt.show()


