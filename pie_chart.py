import matplotlib.pyplot as plt

land = 'Agricultural-land','Built-up-land','Forest-land','Grass/grazing-land','wastelands','waterbodies','other'
area =[42.23,1.15,33.41,1.8,3.07,5.31,11.47]

#creating figure of chart
fig1, ax1 = plt.subplots()

print("plastic in the ocean statistics and Facts")
#autopct for displaying % value
ax1.pie(area, labels = land, autopct ='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')

#display chart
plt.show()