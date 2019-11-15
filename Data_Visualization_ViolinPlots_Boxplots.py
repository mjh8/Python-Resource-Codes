# Violin Plots ->

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

# Run Separate ->

w = sns.boxplot(data=movies, x='Genre', y='CriticRating')

z = sns.violinplot(data=movies, x='Genre', y='CriticRating')


# Try Running Together ->

w = sns.boxplot(data=movies, x='Genre', y='CriticRating')
z = sns.violinplot(data=movies, x='Genre', y='CriticRating')

# Violin Plot = Width - Box plot doesnt show that. Tries with quartiles

z = sns.boxplot(data=movies[movies.Genre=='Drama'], x='Year', y='CriticRating')

z = sns.violinplot(data=movies[movies.Genre=='Drama'], x='Year', y='CriticRating')












