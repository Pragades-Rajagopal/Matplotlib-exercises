# import matplotlib.pyplot as plt

# print(plt.style.use('fivethirtyeight'))

# minutes = [1,2,3,4,5,6,7,8,9]

# pl1 = [1,1,1,2,2,3,3,3,4]
# pl2 = [1,2,2,1,3,4,4,2,3]
# pl3 = [2,1,4,3,5,1,3,2,2]

# labels = ['Player1', 'Player2', 'Player3']
# colors = ['#6d904f','#fc4f30','#008fd5']

# plt.stackplot(minutes, pl1, pl2, pl3, labels= labels, colors= colors)

# plt.legend(loc='upper left')
# plt.title('Stackplots')

# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

popularity = [1,2,3,4,5]

language1 = [59219, 55466, 47544, 36443, 35917]
language2 = [31991, 27097, 23030, 20524, 18523]
language3 = [18017, 7920, 7331, 7201, 5833]

labels = ['User1', 'User2', 'User3']

plt.stackplot(popularity, language1, language2, language3, labels= labels)

plt.legend()
plt.title('Language stackplot')

plt.tight_layout()
plt.show()


