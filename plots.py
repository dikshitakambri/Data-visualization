import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

filepath = "C:/Users/hp/Documents/Data visualization/Data/Iris_Data.csv"
data = pd.read_csv(filepath)

#scatterplot

plt.plot(data.petal_length,data.petal_width,marker='o',ls=' ',label='petal')
plt.plot(data.sepal_length,data.sepal_width,marker='o',ls=' ',label='petal',)

#histogram

plt.hist(data.sepal_length,bins=30)

#barplot

fig, ax = plt.subplots()

ax.barh(np.arange(10),data.sepal_length[:10])

ax.set_yticks(np.arange(0.4,10.4,1))
ax.set_yticklabels(np.arange(1,11))
ax.set(xlabel='xlabel',ylabel='ylabel', title='Title')

#Incorporating statistical data

data.groupby('species').mean().plot(color=['red','blue','yellow','green'],figsize=(6,6),fontsize=10.0)

#statistical plot using seaborn

sns.jointplot(x='sepal_length', y='sepal_width', data=data, height=5)

sns.pairplot(data, hue='species', height=3)
plt.show()
