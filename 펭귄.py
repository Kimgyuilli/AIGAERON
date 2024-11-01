import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pen = sns.load_dataset('penguins')
sns.barplot(x = 'species', y='body_mass_g', data=pen, hue='sex')
plt.show()