import time
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_excel('C:\\Users\\SYED ZAHIRA\\Documents\\ML-lr.xls')
df.head()

df.info()

df.describe()

print(df.columns)

sns.pairplot(df)
plt.show()
time.sleep(10)

sns.distplot(df['Product Price'])
plt.show()

sns.heatmap(df.corr(),annot=True) # annot=True is for the values inside the squares
plt.show()

print(df.columns)

X = df[['Unnamed: 0', 'Id', 'Serial no', 'Salary', 'Product Price', 'Profit']]
y = df['Product Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42) # test_size and random_state is optional

lm = LinearRegression()

# performs the task to predict a dependent variable value (y) based on a given independent variable (x)
lm.fit(X_train, y_train)

# coefficient
print(lm.coef_)

print(X_train.columns)

cdf = pd.DataFrame(lm.coef_,X.columns, columns = ['Coeff'])
print(cdf)

boston = load_boston()
boston.keys()
print(boston['DESCR'])

# predictions
predictions = lm.predict(X_test)
print(predictions)

plt.scatter(y_test, predictions)
plt.show()

sns.distplot((y_test-predictions))
plt.show()

metrics.mean_absolute_error(y_test,predictions)

metrics.mean_squared_error(y_test,predictions)

np.sqrt(metrics.mean_squared_error(y_test,predictions))