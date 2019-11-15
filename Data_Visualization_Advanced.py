import pandas as pd

movies = pd.read_csv('Movie-Ratings.csv')

movies.head()
movies.info()
movies.describe()

# You don't want to treat year as a number. Treat it like a category.
# Convert to a Categorical Variable.

movies.Film = movies.Film.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')

movies.info()
movies.describe()