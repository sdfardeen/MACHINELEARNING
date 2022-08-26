# seaborn is a statical plotting library, has deffault styles,designed to work padas dataframe
# distribution plots

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

tips = sns.load_dataset('tips')
tips.head()

# Returns the Axes object with the plot
sns.distplot(tips['total_bill'])
plt.show()

# to remove kernal density estimation(kde)
sns.distplot(tips['total_bill'], kde=False)
plt.show()

# bins parameter is used to size the bars
sns.distplot(tips['total_bill'], kde=False, bins=50)
plt.show()

# to combine two different distribution plots, 'kind' parameter is which type of plot will be used to compare, default "kind=scatter"
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
plt.show()

sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
plt.show()

# jointplot with kernal density estimation plot
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
plt.show()

sns.jointplot(x='total_bill', y='tip', data=tips)
plt.show()

# to combine and compare all numeric values
sns.pairplot(tips, hue='sex')
plt.show()

# palette parameter assigned 'coolwarm' to trasparent the graph
sns.pairplot(tips, hue='sex', palette='coolwarm')
plt.show()

# rug plot draws a dash mark for every points on this uniform or unique variant distribution
sns.rugplot(tips['total_bill'])
plt.show()

# create a dataset
dataset = np.random.randn(25)
# create another rugplot
sns.rugplot(dataset)
# setup  the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2
# 100 equally spaced points from x_min ti x_max
x_axis = np.linspace(x_min, x_max, 100)
url = 'https://en.wikipedia.org/wiki/Kernal_density_estimation#Practical_estimation_of_the_bandwidth'
bandwidth = ((4 * dataset.std() ** 5) / (3 * len(dataset))) ** .2
# create an empty kernal list
kernal_list = []
# plot each basis function
for data_point in dataset:
    # create a kernal for each point and append to list
    kernal = stats.norm(data_point, bandwidth).pdf(x_axis)
    kernal_list.append(kernal)
    # scale for plotting
    kernal = kernal / kernal.max()
    kernal = kernal * .4
    plt.plot(x_axis, kernal, color='grey', alpha=0.5)

plt.ylim(0, 1)

# kde plot of 'total bill'
sns.kdeplot(tips['total_bill'])
plt.show()

# categorical plots

sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
plt.show()

# to count the occurences
sns.countplot(x='sex', data=tips)
plt.show()

sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips)
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=False)
plt.show()

# issue with sripplot is can't really find how many points are stacked on top of each other
sns.stripplot(x='day', y='total_bill', data=tips)
plt.show()

# jitter is to seperate these stack points
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)
plt.show()

sns.stripplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
plt.show()

# swarmplot is the combo of violin and stripplot
# drawback of swarmplot, sometims don't scale the large numbers
sns.swarmplot(x='day', y='total_bill', data=tips)
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, color='black')
plt.show()

sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')
plt.show()

# matrix plots

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()

flights.head()

tc = tips.corr()
print(tc)

sns.heatmap(tc, annot=True, cmap='coolwarm')
plt.show()

fp = flights.pivot_table(index='month', columns='year', values='passengers')

sns.heatmap(fp)
plt.show()

sns.heatmap(fp, cmap='coolwarm', linecolor='white', linewidths=5)
plt.show()

# cluster is to show the columns and rows are similar to each other
sns.clustermap(fp)
plt.show()

sns.clustermap(fp, standard_scale=1)
plt.show()

# grids

iris = sns.load_dataset('iris')
iris.head()

# to know unique data\
iris['species'].unique()

sns.pairplot(iris)
plt.show()

# this gives empty grids
sns.PairGrid(iris)
plt.show()

# if scatter plot is wanted
g = sns.PairGrid(iris)
g.map(plt.scatter)
plt.show()

g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
plt.show()

g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(plt.scatter, 'total_bill', 'tip')
plt.show()

# regression plots

tips = sns.load_dataset('tips')
tips.head()

# lmplot(linear model plot)
sns.lmplot(x='total_bill', y='tip', data=tips)
plt.show()

# to set the ration of the grid
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', aspect=0.6)
plt.show()

# changing marker size and shape
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', aspect=0.6, markers=['o', 'v'], scatter_kws={'s': 50})
plt.show()

# styling and coloring

tips = sns.load_dataset('tips')
tips.head()

# .set_style(style: 'darkgrid', 'white', 'ticks', 'whitegrid', 'dark')
sns.set_style('darkgrid')
sns.countplot(x='sex', data=tips)
plt.show()

# setting grid style
sns.set_style('darkgrid')
# setting figure and font size
sns.set_context('notebook',font_scale=1)
sns.countplot(x='sex', data=tips)
plt.show()

# setting grid style
sns.set_style('darkgrid')
# setting figure and font size
sns.set_context('poster', font_scale=1)
sns.countplot(x='sex', data=tips)
plt.show()

# there a color palettes in matplotlib
# one of the palettes is 'seismic'
sns.lmplot(x='total_bill', data=tips, y='tip', hue='sex', palette='seismic')
plt.show()

