import pandas as pd
import matplotlib.pyplot as plt

filepath = "C:/Users/hp/Documents/Vizualization/Data/Iris_Data.csv"
data = pd.read_csv(filepath)

#scatterplot
plt.plot(data.petal_length,data.petal_width,marker='o',ls=' ',label='petal')
plt.plot(data.sepal_length,data.sepal_width,marker='o',ls=' ',label='petal')

#histogram
plt.hist(data.sepal_length,bins=30)
plt.show()