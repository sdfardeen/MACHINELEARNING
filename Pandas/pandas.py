import pandas as pd
import numpy as np

DF = pd.read_excel("C:\\Users\\SYED ZAHIRA\\OneDrive\\Documents\\Book1.xls")
DF.head()
# printing the heads in xls file
DF.insert(3,'Team', 'RedBull')
# inserting a new column name of "Team"
# syntax of insert is <<< Dataframe.insert(loc, column, value, allow_duplicates = "False") >>>
print(DF)
# inserting a column using 'for' loop
new_title = pd.Series([])
for i in range(len(DF)):
    if DF["Type"][i] == "alphabet":
        new_title = "ALFA"
    elif DF["Type"][i] == "Alpha":
        new_title = "ALFA"
    else:
        new_title[i] = DF["Type"][i]

DF.insert(3, 'Challenges', new_title)
DF.head()

np.random.seed(20)
df = pd.DataFrame(np.random.rand(3, 3), columns =['A', 'B', 'C'])
df
# creating random integers in given range of given column structure
