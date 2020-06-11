import matplotlib.pyplot as plt
import pandas
import random
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_val = []
y_val = []

index = count()

def animate(i):
    x_val.append(next(index))
    y_val.append(random.randint(0,5))

    plt.plot(x_val, y_val)


a = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()