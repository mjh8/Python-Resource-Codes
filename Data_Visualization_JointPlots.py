import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')

# Jointplots

movies = pd.read_csv('Movie-Ratings.csv')

j = sns.jointplot(data=movies, x='CriticRating', y='AudienceRating')

# BiVarient Distribution

j = sns.jointplot(data=movies, x='CriticRating', y='AudienceRating', kind='hex')

