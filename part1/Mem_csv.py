import csv

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

for line in csv_file:
    print(line)