# Histogram Final Touches ->

# Import Libraries ->

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


# Original Histogram ->

list1 = list()
mylabels = list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions) 
    mylabels.append(gen)
h = plt.hist(list1, bins=30, stacked=True, rwidth=1, label=mylabels)
plt.legend()
plt.show()



# Improved Histogram ->

sns.set_style("whitegrid")
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)

list1 = list()
mylabels = list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions) 
    mylabels.append(gen)
h = plt.hist(list1, bins=30, stacked=True, rwidth=1, label=mylabels)
plt.title("Movie Budget Distribution", fontsize=20,
          color="darkblue", fontname='Console')
plt.ylabel("Number of Movies", fontsize=15, color="Red")
plt.xlabel("Budget", fontsize=15, color="Green")
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.legend(frameon=True, fancybox=True, shadow=True, 
           framealpha=1, prop={'size':18})
plt.show()