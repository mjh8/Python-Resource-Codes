# Building Dashboards

# Import ->

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



# Building a Dashboard ->
# Run all the code below Together ->>>

sns.set_style("darkgrid")
f, axes = plt.subplots(2, 2, figsize=(12,12))

k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, 
                 ax=axes[0,0])

k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, 
                 ax=axes[0,1])

k1.set(xlim=(-20,160))
k2.set(xlim=(-20,160))

z = sns.violinplot(data=movies[movies.Genre=='Drama'], 
                   x='Year', y='CriticRating', ax=axes[1,0])

k1 = sns.kdeplot(movies.CriticRating, movies.AudienceRating,
                 shade=True, shade_lowest=False, cmap='Reds',
                 ax=axes[1,1])

k1b = sns.kdeplot(movies.CriticRating, movies.AudienceRating,
                  cmap='Reds', 
                  ax=axes[1,1])

plt.show()



# Styling a Dashboard ->
# Run all the code below Together ->>>

sns.set_style("dark", {"axes.facecolor": "black"})
f, axes = plt.subplots(2, 2, figsize=(8,8))

# Plot 0,0
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, 
                 shade=True, shade_lowest=True, cmap='inferno',
                 ax=axes[0,0])

k1b = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, 
                  cmap='cool', 
                  ax=axes[0,0])

# Plot 0,1
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, 
                 shade=True, shade_lowest=True, cmap='inferno',
                 ax=axes[0,1])

k2b = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, 
                 cmap='cool', 
                 ax=axes[0,1])

# Plot 1,0
z = sns.violinplot(data=movies, 
                   x='Year', y='BudgetMillions', 
                   palette='YlOrRd',
                   ax=axes[1,0])

# Plot 1,1
k4 = sns.kdeplot(movies.CriticRating, movies.AudienceRating,
                 shade=True, shade_lowest=False, cmap='Blues_r',
                 ax=axes[1,1])

k4b = sns.kdeplot(movies.CriticRating, movies.AudienceRating,
                  cmap='gist_gray_r', 
                  ax=axes[1,1])

k1.set(xlim=(-20,160))
k2.set(xlim=(-20,160))
plt.show()




# Finishing Touches ->
# Run all the code below Together ->>>

sns.set_style("dark", {"axes.facecolor": "black"})
f, axes = plt.subplots(2, 2, figsize=(8,8))

# Plot 0,0
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, 
                 shade=True, shade_lowest=True, cmap='inferno',
                 ax=axes[0,0])

k1b = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, 
                  cmap='cool', 
                  ax=axes[0,0])

# Plot 0,1
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, 
                 shade=True, shade_lowest=True, cmap='inferno',
                 ax=axes[0,1])

k2b = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, 
                 cmap='cool', 
                 ax=axes[0,1])

# Plot 1,0
z = sns.violinplot(data=movies, 
                   x='Year', y='BudgetMillions', 
                   palette='YlOrRd',
                   ax=axes[1,0])

# Plot 1,1
k4 = sns.kdeplot(movies.CriticRating, movies.AudienceRating,
                 shade=True, shade_lowest=False, cmap='Blues_r',
                 ax=axes[1,1])

k4b = sns.kdeplot(movies.CriticRating, movies.AudienceRating,
                  cmap='gist_gray_r', 
                  ax=axes[1,1])

k1.set(xlim=(-20,160))
k2.set(xlim=(-20,160))
plt.show()









