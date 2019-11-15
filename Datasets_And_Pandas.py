# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:18:28 2019

@author: mheidenreich
"""

# Pandas used for Dataframes
# Numpy used for Scientific Computing
# ScikitLearn used for Machine Learning and Stats

import pandas as pd

stats = pd.read_csv('Demographic-Data.csv')

# Length of Rows
len(stats)

# See Columns
stats.columns

# Number of Columns
len(stats.columns)

# Top 5 Rows
stats.head()
stats.head(10)

# Object Oridented Programming - Python
# Vectorized Programming - R

# Bottom 5 Rows
stats.tail()

# Information
stats.info() # Similar to STR function in R

# Get Stats
stats.describe()
stats.describe().transpose()



# Subsetting Dataframes
stats.head()

# Rows
stats[21:26]
stats[185:]
stats[::-1] #Reverse order of rows
stats[::20] #Everything 20th Row

# Columns

stats[['Country Name', 'Country Code']][4:8]

stats.head()

# Math Operations

stats['MyCalc'] = stats.Birth rate * stats.Internet users









































