import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn')

# x = [2,5,8,3,6]
# y = [3,8,2,4,9]

# colors = [7,3,2,6,9]

# plt.scatter(x,y, s= 100, c=colors, edgecolors='black', 
#             cmap='Greens', alpha=0.60)

data = pd.read_csv('Viewer_count.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio, s=ratio, edgecolors='black', 
            cmap='summer', alpha=0.8)

cbar = plt.colorbar()
cbar.set_label('Likes/Dislikes')

plt.xscale('log')
plt.yscale('log')

plt.title('Youtube viewers')
plt.xlabel('View count')
plt.ylabel('Likes')

plt.show()