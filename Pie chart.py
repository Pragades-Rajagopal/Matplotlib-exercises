import matplotlib.pyplot as p

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

explode = [0,0,0,0.1,0]

p.pie(slices, labels= labels, shadow= True, wedgeprops={'edgecolor':'black'},
    startangle= 90, explode= explode, autopct='%1.1f%%', radius= 1)

p.title('Pie chart')

p.tight_layout()
p.show()