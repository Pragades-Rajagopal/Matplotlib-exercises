import csv
import random
import time

x = 0
a = 1000
b = 1000

fields = ['x', 'a', 'b']

with open('counter.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
    csv_writer.writeheader()

while True:

    with open('counter.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fields)

        info = {
            'x' : x,
            'a' : a,
            'b' : b
        }

        csv_writer.writerow(info)
        print(x,a,b)

        x += 1
        a = a + random.randint(-6, 8)
        b = b + random.randint(-6, 5)

    time.sleep(0.001)