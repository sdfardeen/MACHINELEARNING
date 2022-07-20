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
print(df)
# creating random integers in given range of given column structure

df.add(1)
# adding 1(value) to all

df1 = pd.DataFrame({"A":[1, 5, 3, 4, 2],
                   "B":[3, 2, 4, 3, 4],
                   "C":[2, 2, 7, 3, 4],
                   "D":[4, 3, 6, 12, 7]},
                   index =["A1", "A2", "A3", "A4", "A5"])

print(df1)

sr = pd.Series([12, 25, 64, 18], index =["A", "B", "C", "D"])
sr
# creating a series with given elements in axis

df.sub(sr, axis=1)
# .sub() is used substract each element by given axis, here the axis=1 it means the susbtraction is done in horizontal axis by each elements of 'df'&'sr'
df.mul(sr, axis=1)
# we're multiplying the elements by using .mul()
df.div(2,fill_value=50)
# dividing the elements with fill value
df.div(sr,axis=1)
# dividing the elements by using axis
print(df1)

df1.nunique(axis=1)
# getting unique values across axis=1(row)
df1.nunique(axis=0)
# getting unique values across axis=0(column)

nill = pd.read_excel("C:\\Users\\SYED ZAHIRA\\OneDrive\\Documents\\Book1.xls")
bool_series = pd.isnull(nill["Title"])
nill[bool_series]

new = nill["Title"].isin(["DEF"])
nill[new]
# pd.isin() returns the value that data inthe file, returns Boolean dtype

nill.sort_index(axis=0)
# sorting the index labels

csv = pd.read_csv("C:\\Users\\SYED ZAHIRA\\Downloads\\nba.csv", index_col = "Name")
loc = csv.loc["Avery Bradley"]
print(loc)

