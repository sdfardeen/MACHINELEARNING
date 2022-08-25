import pandas as pd
import matplotlib.pyplot as plt
# importing Pandas and matplotlib libraries

# to read excel file
sales = pd.read_excel('C:\\Users\\SYED ZAHIRA\\OneDrive\\Documents\\Book1.xls', parse_dates=['Type'])

# sales.head() is printing all heads in the data
sales.head()

# printing the data structure
print(sales.shape)

# printing the data's information
print(sales.info)

# printing descriptive statistics of given data
print(sales.describe)

# printing descriptive statistics of "Price" col
sales['Price'].describe()

# printing the Mean of the "Price" col
sales['Price'].mean()

# printing the Median of the "Price" col
sales['Price'].median()
# printing the 'box' kind plot of "Price" col
sales['Price'].plot(kind='box', vert=False, figsize=(10,2))
plt.show()

# printing the 'density' kind plot of "Price" col ; 'density' plot gives Density Estimation plot
sales['Price'].plot(kind='density', figsize=(10,2))
plt.show()

# printing the 'density' kind plot with 'mean' with red color and 'median' with green color of "Price" col
ax = sales['Price'].plot(kind='density', figsize=(10,2))
ax.axvline(sales['Price'].mean(), color='red')
ax.axvline(sales['Price'].median(), color='green')
plt.show()

# printing 'hist' kind plot by setting labels for X-Y axis ; hist' plot gives histogram about the data in "Price" col
ax = sales['Price'].plot(kind='hist', figsize=(10,2))
ax.set_ylabel('Number of Sales')
ax.set_xlabel('dollars')
plt.show()

# printing the count values of "customer age"col
sales['Customer Age'].value_counts()
# printing 'pie' kind plot with count values of "customer age"col ; 'pie' kind gives pie plot
sales['Customer Age'].value_counts().plot(kind='pie', figsize=(6,6))
plt.show()

# printing 'bar' kind plot with count values of "customer age"col ; 'bar' kind gives vertical bar plot
sales['Customer Age'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Number of sales')
plt.show()

# printing the corelation of given data
cor = sales.corr()
print(cor)

# printing the given data into pixel show and assigning the labels
# xticks will set the labels of the x-axis's in vertical or horizontal
# yticks will set the labels of the y-axis's in vertical or horizontal
fig=plt.figure(figsize=(8,8))
plt.matshow(cor, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(cor.columns)), cor.columns, rotation='vertical')
plt.yticks(range(len(cor.columns)), cor.columns)
plt.show()

# printing the "revenue" col in Y-axis and "customer age" col in X-axis 'scatter' kind plot
sales.plot(kind='scatter', x='Customer Age', y='Revenue', figsize=(6,6))
plt.show()

# printing the "revenue" col in X-axis and "Profit" col in Y-axis 'scatter' kind plot
sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6,6))
plt.show()

# printing the 'box' kind plot with "Profit" and "customer age" cols
ax = sales[['Profit', 'Customer Age']].boxplot(by='Customer Age', figsize=(10,6))
plt.show()

# printing box plots with the layouts of (rows=2, cols=3)
boxplot_col = ['Customer Age', 'Price', 'Profit', 'Revenue']
sales[boxplot_col].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))
plt.show()

# printing heads of revenue/customer age values
sales['Revenue per age'] = sales['Revenue'] / sales['Customer Age']
sales['Revenue per age'].head()
plt.show()

# printing the 'density' kind plot of "Revenue per age" col
sales['Revenue per age'].plot(kind='density',figsize=(14,6))
plt.show()

# printing the 'hist' kind plot of "Revenue per age" col
sales['Revenue per age'].plot(kind='hist',figsize=(14,6))
plt.show()
