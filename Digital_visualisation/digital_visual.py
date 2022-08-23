import pandas as pd
import matplotlib.pyplot as plt

book=pd.read_excel('C:\\Users\\SYED ZAHIRA\\OneDrive\\Documents\\Book1.xls')
book.head()

# histogram plot
plt.hist(book['Price'])
plt.show()

plt.hist(book['Customer Age'])
plt.show()

plt.hist(book['Revenue'])
plt.show()

plt.hist(book['Profit'])
plt.show()

#scatter plot
plt.scatter(book['Price'],book['Profit'])
plt.xlabel('Profit')
plt.ylabel('Price')
plt.show()

# combining scatter,plot
plt.scatter(book['Price'],book['Profit'])
plt.plot(book['Price'],book['Profit'],color='r')
plt.title('Scatter plot')
plt.xlabel('Profit')
plt.ylabel('Price')
plt.show()

# donut plot
pie1=plt.pie(book['Price'],autopct='%0.1F%%', radius=2)
pie2=plt.pie([5], colors='w',radius=1.5)
pie2=plt.pie(book['Profit'],colors=['black','grey','pink','green','red','purple','brown','yellow','orange'],radius=1,autopct='%0.1F%%')
plt.show()

# area plot
x=[10,20,30,40,50,60,70,80,90]
plt.stackplot(x,book['Price'])
plt.plot(x,book['Price'],color='black')
plt.title('Area plot')
plt.xlabel('x-axis')
plt.ylabel('Price')
plt.show()

