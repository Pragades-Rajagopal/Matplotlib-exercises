import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')


x = [2,4,6,8,10]
ind_x = np.arange(len(x))
widthx = 0.25

y = [102,109,250,302,354]
z = [153,208,300,384,460]
w = [200, 289, 356, 460, 550]

plt.bar(ind_x - widthx ,y, width= widthx, label = 'C++', color = "#444444")
plt.bar(ind_x,z, width= widthx, label = 'Python', color = "#008fd5")
plt.bar(ind_x + widthx ,w, width= widthx, label = 'Matlab', color = "#e5ae38")

plt.legend()

plt.xlabel('Years')
plt.ylabel('Salary')
plt.title('Salary hike')

plt.grid('true')

plt.xticks(ticks= ind_x, labels=x)

plt.tight_layout()
plt.savefig('salary.png')
plt.show()
