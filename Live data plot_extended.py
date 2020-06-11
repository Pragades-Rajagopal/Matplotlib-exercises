import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

plt.style.use('fivethirtyeight')

def animate(i):

    data = pd.read_csv('counter.csv')

    x = data['x']
    y1 = data['a']
    y2 = data['b']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Price graph')

    plt.tight_layout()

anime = FuncAnimation(plt.gcf(), animate, interval=1)

plt.tight_layout()
plt.show()