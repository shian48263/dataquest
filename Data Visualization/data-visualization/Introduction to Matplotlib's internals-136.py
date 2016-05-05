## 2. Levels of abstraction ##

import matplotlib.pyplot as plt
%matplotlib inline

# 2 simple lists of values
month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

plt.scatter(month, temperature)
plt.show()

## 4. Figures and Subplots ##

fig = plt.figure(figsize=(5,7))
ax = fig.add_subplot(1,1,1)
plt.show()

# Print the types
print(type(fig))
print(type(ax))

## 5. Axes ##

import numpy as np
month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([np.min(month), np.max(month)])
ax.set_ylim([np.min(temperature), np.max(temperature)])
plt.show()

## 6. Adding data ##

import numpy as np

month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([np.min(month),np.max(month)])
ax.set_ylim([np.min(temperature), np.max(temperature)])

color = 'darkblue'
marker = 'o'

# run the .scatter() method, params: color, marker
ax.scatter(month, temperature, color=color, marker=marker)
plt.show()

## 7. Customizing the plot ##

import numpy as np

month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([np.min(month)-1,np.max(month)+1])
ax.set_ylim([np.min(temperature)-5, np.max(temperature)+5])
ax.set_xlabel('Month')
ax.set_ylabel('Temperature')
ax.set_title('Year Round Temperature')

color = 'darkblue'
marker = 'o'

# run the .scatter() method, params: color, marker
ax.scatter(month, temperature, color='darkblue', marker='o')
plt.show()

## 8. Setting multiple attributes easily ##

month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set(xlim=(0,13), ylim=(10,110), xlabel='Month', ylabel='Temperature', title='Year Round Temperature')
ax.scatter(month, temperature, color='darkblue', marker='o') #add xlabel, ylabel, and title
plt.show()

## 9. Multiple subplots ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

## 10. Adding data to multiple subplots ##

month_2013 = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature_2013 = [32,18,40,40,50,45,52,70,85,60,57,45]
month_2014 = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature_2014 = [35,28,35,30,40,55,50,71,75,70,67,49]

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.set(xlim=(0,13), ylim=(10,110), title='2013')
ax2.set(xlim=(0,13), ylim=(10,110), title='2014')
ax1.scatter(month_2013, temperature_2013, color='darkblue', marker='o')
ax2.scatter(month_2014, temperature_2014, color='darkgreen', marker='o')
plt.show()