
# KDE Plot ->

# Kernel Density Estimate Plot

import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')

movies = pd.read_csv('Movie-Ratings.csv')

movies = pd.read_csv('Movie-Ratings.csv', dtype={'Film':'category',
                                                 'Genre':'category',
                                                 'Year':'category'})

vis1 = sns.lmplot(data=movies, x='CriticRating', y='AudienceRating',
                      fit_reg=False, hue='Genre',
                      size=7, aspect=1)

k1 = sns.kdeplot(movies.CriticRating, movies.AudienceRating,
                 shade=True, shade_lowest=False, cmap='Reds')

k1b = sns.kdeplot(movies.CriticRating, movies.AudienceRating,
                 cmap='Reds')

# Run Together ->
k1 = sns.kdeplot(movies.CriticRating, movies.AudienceRating,shade=True, shade_lowest=False, cmap='Reds')
k1b = sns.kdeplot(movies.CriticRating, movies.AudienceRating,cmap='Reds')







































