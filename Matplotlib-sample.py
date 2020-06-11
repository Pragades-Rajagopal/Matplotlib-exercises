import csv
import matplotlib.pyplot as p
from collections import Counter as c

with open('data.csv') as csv_file:
    csv_read = csv.DictReader(csv_file)

    lang_count = c()

    for i in csv_read:
        lang_count.update(i['LanguagesWorkedWith'].split(';'))

print (lang_count.most_common(5))

lang = []
user = []

for x in lang_count.most_common(5):
    lang.append(x[0])
    user.append(x[1])

print(lang)
print(user)
