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
plt.show()
