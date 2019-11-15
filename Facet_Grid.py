# Facet Grid ->

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


# Splitting up a visualization based on a rule

g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')

plt.scatter(movies.CriticRating, movies.AudienceRating)

# Now map scatter plot onto Facet Grid

g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating')

# Can populate with any type of chart

# Histograms

g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
g = g.map(plt.hist, 'CriticRating')

g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
g = g.map(plt.hist, 'BudgetMillions')



# Pass Keyword Arguments to Scatterplot

g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kws = dict(s=50, linewidth=0.5, edgecolor='black')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating', **kws)



# Controlling Axis - Adding Diagonals

g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kws = dict(s=50, linewidth=0.5, edgecolor='black')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating', **kws)
g.set(xlim=(0,100), ylim=(0,100))
for ax in g.axes.flat:
    ax.plot((0,100), (0,100), c='grey', ls="--")
g.add_legent()