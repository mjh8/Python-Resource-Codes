import pandas as pd

stats = pd.read_csv('Demographic-Data.csv')

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.figsize'] = 8,4

vis1 = sns.distplot(stats['InternetUsers'], bins = 30)

vis2 = sns.boxplot(data=stats, x="IncomeGroup", y="BirthRate")


vis3 = sns.lmplot(data=stats, x="InternetUsers", y="BirthRate")
vis3 = sns.lmplot(data=stats, x="InternetUsers", y="BirthRate", fit_reg=False)
# Correlation does not imply causation. 

vis3 = sns.lmplot(data=stats, x="InternetUsers", y="BirthRate",
                  fit_reg=False, hue='IncomeGroup', size=10, aspect=1, scatter_kws={"s":10})












