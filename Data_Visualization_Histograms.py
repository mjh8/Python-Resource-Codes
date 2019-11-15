# Histograms

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

movies.head()
movies.describe()


# Seaborn ->


# sns.set_style("white")
sns.set_style("darkgrid")
# style must be one of white, dark, whitegrid, darkgrid, ticks

# Seaborn Histogram
m1 = sns.distplot(movies.AudienceRating, bins=15)

#Pyplot Histogram
n1 = plt.hist(movies.AudienceRating, bins=15)

n2 = plt.hist(movies.CriticRating, bins=15)

# Run Together:
n1 = plt.hist(movies.AudienceRating, bins=15)
n2 = plt.hist(movies.CriticRating, bins=15)



# Stacked Histograms ->

plt.hist(movies.BudgetMillions)

# or

plt.hist(movies.BudgetMillions)
plt.show()




# Filtering Dataset to Build Historgram

# Step1
movies.Genre == 'Drama'

# Step2
movies[movies.Genre == 'Drama']

# Step3
movies[movies.Genre == 'Drama'].BudgetMillions

# Step4
plt.hist(movies[movies.Genre == 'Drama'].BudgetMillions)


# Graphs are overlayed over each other. 
plt.hist(movies[movies.Genre == 'Action'].BudgetMillions, bins=15)
plt.hist(movies[movies.Genre == 'Drama'].BudgetMillions, bins=15)
plt.hist(movies[movies.Genre == 'Thriller'].BudgetMillions, bins=15)
plt.show()

# Stack the Histograms ->

plt.hist([movies[movies.Genre == 'Action'].BudgetMillions, 
          movies[movies.Genre == 'Drama'].BudgetMillions], 
                bins=15, stacked=True)
plt.show()


# Add a Loop ->

for gen in movies.Genre.cat.categories:
    print(gen)

# Histogram with Loop ->

list1 = list()
mylabels = list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions) 
    mylabels.append(gen)
    # The append function updates list1, so need to add a list1 = at the beginning
print(list1)
    
h = plt.hist(list1, bins=30, stacked=True, rwidth=1, label=mylabels)
plt.legend()
plt.show()
























