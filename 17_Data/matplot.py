import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

''' -->
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y, "o--b")
plt.axis([0,6,0,20])

plt.title("Graph Title")
plt.xlabel("x label")
plt.ylabel("y label")

plt.show()
'''

''' -->
x = np.linspace(0,2,100)

plt.plot(x, x, label = "linear")
plt.plot(x, x**2, label = "quadratic")
plt.plot(x, x**3, label = "cubic")

plt.xlabel("x label")
plt.ylabel("y label")
plt.legend()

plt.title("Simple Plot")

plt.show()
'''

''' -->
x = np.linspace(0,2,100)
fig, axs = plt.subplots(3) # iki farklı düzlemler

axs[0].plot(x, x, color = "r")
axs[0].set_title("linear")

axs[1].plot(x, x**2, color ="b")
axs[1].set_title("quadratic")

axs[2].plot(x, x**3, color ="y")
axs[2].set_title("cubic")

plt.tight_layout()

plt.show()

'''

''' -->
x = np.linspace(0,2,100)
fig, axs = plt.subplots(2,2)

fig.suptitle("Graph Title")

axs[0,0].plot(x, x, color = "r")
axs[0,1].plot(x, x**2, color = "g")
axs[1,0].plot(x, x**3, color = "y")
axs[1,1].plot(x, x**4, color = "b")

plt.show()

'''

'''--> 

df = pd.read_csv('C:/Users/SefaPc/Desktop/btkPythonL/17_Data/datasets/nba.csv')

df = df.drop(['position', 'name', 'height','birth_date'], axis = 1).groupby('college').mean().head(10)

df.plot(subplots=True)
plt.legend()

plt.show()

'''

#--> Figure olusturma

''' -->
x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

figure = plt.figure()

axes_cube = figure.add_axes([0.1, 0.1, 0.9, 0.9]) # soldan %20 sağa doğru grafiği getir

axes_cube.plot(x, y, 'b')
axes_cube.set_xlabel("x axis")
axes_cube.set_ylabel("y axis")
axes_cube.set_title("cube")


axes_square = figure.add_axes([0.15, 0.6, 0.25, 0.25])
axes_square.plot(x, z, 'r')
axes_square.set_xlabel("x axis")
axes_square.set_ylabel("y axis")
axes_square.set_title("square")

plt.show()

'''

''' -->

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

figure = plt.figure()

axes = figure.add_axes([0.2,0.2,0.6,0.6])

axes.plot(x,z, label="Square")
axes.plot(x,y, label = "Cube")
axes.legend(loc = 4)

plt.show()

'''

''' -->

fig, axes = plt.subplots(nrows= 2, ncols= 1, figsize=(8,8)) # figsize figürün boyutunu belirler
x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure1.pdf") # verilen boyutta kaydedilir

plt.show()

'''

#--> Grafik Türleri

yil = [2011, 2012, 2013, 2014, 2015]
oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,9]

# Stack Plot
'''
plt.plot([], [], color = "y", label = "Player 1")
plt.plot([], [], color = "g", label = "Player 2")
plt.plot([], [], color = "r", label = "Player 3")

plt.stackplot(yil, oyuncu1, oyuncu2, oyuncu3, colors=['y','g','r'])
plt.title("Goals scored by year")
plt.xlabel("Year")
plt.ylabel("Score")

plt.legend()

plt.show()
'''

# Pie Graph
'''
goal_types = "Penalty", "Goal", "Freekick"
goals = [12,35,7]
colors = ['y', 'r', 'b']

plt.pie(goals, labels = goal_types, colors= colors, shadow=True, explode=(0.05,0.05,0.05), autopct="%1.1f%%") # Gölgeleme, dilimler arası boşluk, yazacak olan yüzdeklik ifade 

plt.show()
'''

# Bar Graph
'''
plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50,40,70,80,20], label = "BMW", width=.5)
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80,20,20,50,60], label = "Audi", width=.5)

plt.legend()
plt.xlabel("Days")
plt.ylabel("Distance (Km)")
plt.title("Car Details")

plt.show()
'''

# Histogram
'''
yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,11,115,80,75,65,54,44,43,42,48]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar, yas_gruplari, histtype="bar", rwidth=0.8)

plt.xlabel("Age Groups")
plt.ylabel("Number of People")
plt.title("Histogram Graph")

plt.show()
'''