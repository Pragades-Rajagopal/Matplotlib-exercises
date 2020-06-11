import csv
#import pandas as pd
from collections import Counter as ct
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

with open('data.csv') as csv_file:           
    csv_reader = csv.DictReader(csv_file)

# data = pd.read_csv('data.csv')
# ids = data['Responder_id']
# lang_responses = data['LanguagesWorkedWith']

    lang_count = ct()

    for row in csv_reader:
        lang_count.update(row['LanguagesWorkedWith'].split(';'))

# for r in lang_responses:
#     lang_count.update(r.split(';'))

lang = []
popularity = []

for i  in lang_count.most_common(15):
    lang.append(i[0])
    popularity.append(i[1])

lang.reverse()
popularity.reverse()

plt.barh(lang, popularity)

plt.xlabel('Language')
plt.ylabel('Users')
#plt.title('Language usage')

plt.grid('true')

plt.tight_layout()
plt.show()
