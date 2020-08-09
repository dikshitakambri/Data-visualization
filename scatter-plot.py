import matplotlib.pyplot as plt

land = 'Agricultural-land','Built-up-land','Forest-land','Grass/grazing-land','wastelands','waterbodies','other'
area =[42.23,1.15,33.41,1.8,3.07,5.31,11.47]

plt.scatter(land,area)
plt.show()