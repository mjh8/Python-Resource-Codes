
# Subplots()

# Import Datasets ->

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

# Build Graphs ->

sns.set_style("dark")

k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating)
            
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating)

# Look for skew to left, right, up or down in visualization


# -> Subplots() ->

f, axes = plt.subplots(1, 2)

f, axes = plt.subplots(1, 2, figsize=(12,6))


f, axes = plt.subplots(1, 2, figsize=(12,6))
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0])
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[1])


f, axes = plt.subplots(2, 2, figsize=(10,5))
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0,1])
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[1,0])


f, axes = plt.subplots(1, 2, figsize=(10,5), sharex=True, sharey=True)
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0])
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[1])
k1.set(xlim=(-20,160))