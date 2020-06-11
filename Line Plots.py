import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use('fivethirtyeight')

data = pd.read_csv('salaries.csv')

ages = data['Age']
dev_salaries = data['All_Devs']
py_salary = data['Python']
js_salary = data['JavaScript']

plt.plot(ages, dev_salaries, linestyle= '--', label='All Devs', color= '#444444')

#median = 61500
plt.plot(ages, py_salary, label= 'Python')

plt.fill_between(ages, py_salary, dev_salaries, alpha=0.25,
                where=(py_salary > dev_salaries), interpolate=True, label= 'Above avg')

plt.fill_between(ages, py_salary, dev_salaries, alpha=0.25, color= 'red',
                where=(py_salary <= dev_salaries), interpolate=True, label= 'Below avg')   

median_line = 35
plt.axvline(median_line, color='green', label='Median Age')             

plt.xlabel('Age')
plt.ylabel('Salary(USD)')

plt.legend()
plt.title('Salary Plot')
plt.grid('True')
plt.tight_layout()

plt.savefig('Salary_plot.png')
plt.show()