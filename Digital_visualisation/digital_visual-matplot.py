import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

book = pd.read_excel('C:\\Users\\SYED ZAHIRA\\OneDrive\\Documents\\Book1.xls')
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

# scatter plot
plt.scatter(book['Price'], book['Profit'])
plt.xlabel('Profit')
plt.ylabel('Price')
plt.show()

# combining scatter,plot
plt.scatter(book['Price'], book['Profit'])
plt.plot(book['Price'], book['Profit'], color='r')
plt.title('Scatter plot')
plt.xlabel('Profit')
plt.ylabel('Price')
plt.show()

# donut plot
pie1 = plt.pie(book['Price'],autopct='%0.1F%%', radius=2)
pie2 = plt.pie([5], colors='w', radius=1.5)
pie2 = plt.pie(book['Profit'], colors=['black', 'grey', 'pink', 'green', 'red', 'purple', 'brown', 'yellow', 'orange'], radius=1, autopct='%0.1F%%')
plt.show()

# area plot
x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
plt.stackplot(x, book['Price'])
plt.plot(x, book['Price'], color='black')
plt.title('Area plot')
plt.xlabel('x-axis')
plt.ylabel('Price')
plt.show()

x = np.linspace(0, 5, 11)
y = x**2

print(x)

print(y)

# funtional method
plt.plot(x, y)
plt.show()

plt.plot(x, y, 'r')
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.show()

plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')
plt.show()

# object oriented method
fig=plt.figure()
axe = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axe = fig.add_axes([left,up from bottom,width,height])
axe.plot(x, y)
axe.set_xlabel('X Label')
axe.set_ylabel('Y Label')
axe.set_title('X-Y Labels')
plt.show()

fig = plt.figure()
axe1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axe2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
axe1.plot(x, y)
axe2.plot(y, x)
axe1.set_title('Outer plot')
axe2.set_title('Inner plot')
plt.show()

fig=plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.9, 0.9])
axes.plot(x, y, 'r')
axes.plot(y, x, 'g')
plt.show()

fig, axe = plt.subplots(3, 3)
# axes.plot(x, y)
plt.tight_layout()
# plt.tight_layout() fixes the overlapping of the layouts
plt.show()

fig, axe = plt.subplots(nrows=1, ncols=2)
plt.show()

fig, axe = plt.subplots(1, 2)
for current_axe in axe:
    current_axe.plot(x, y)
plt.show()

fig, axe = plt.subplots(1, 2)
axe[0].plot(x, y, 'g')
axe[1].plot(y, x, 'r')
# plotting in particular box
plt.show()

# figure size and DPI
# customising the figure size
fig = plt.figure(figsize=(3, 2))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
plt.show()

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 2))
ax[0].plot(x, y)
ax[1].plot(y, x, 'r')
plt.show()

fig.savefig('my figure.png', dpi=200)

# location string = location code
# best = 0
# upper right = 1
# upper left = 2
# lower left = 3
# lowerr roght = 4
# right = 5
# cantre left = 6
# centre right = 7
# lower centre = 8
# upper cantre = 9
# centre = 10

fig = plt.figure()
axis = fig.add_axes([0, 0, 1, 1])
axis.plot(x, x**2, label='X squared')
axis.plot(x, x**3, label='X cubed')
axis.legend(loc=1)
plt.show()

# coloring the plot lines and styling the lines
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y, 'orange')  #RGB hex code can also used "ex: #FF8C00"
# coloring the plot lines
plt.show()

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y, 'purple', linewidth=5)
# line thickness "linewidth" or "lw"
plt.show()

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y, 'purple', linewidth=5, alpha=0.25)
# line transparency "alpha"
plt.show()

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y,'purple', linewidth=5, linestyle=':')
# line styling "linestyle" or "ls"
plt.show()

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y, 'purple', linewidth=3, linestyle='-', marker='o', markersize=15, markerfacecolor='yellow', markeredgecolor='green')
# marking the line plots
plt.show()

