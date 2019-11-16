# PYTHON ->

import pyodbc 
import pandas as pd

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SERVERNAME;'
                      'Database=DATABASE;'
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()
cursor.execute('select * from table_name')

for row in cursor:
    print(row)

dataset = pd.read_sql('select field1, field2, field3 from table_name', cnxn)

dataset.head()