import csv

data_array = [['col1', 'col2', 'col3'], [1, 2, 3], [4, 5, 6]]

f = open('numbers.csv', 'w')

with f:

    writer = csv.writer(f)

    for row in data_array:
        writer.writerow(row)

# Read as a List, skip headers

with open('numbers.csv') as f:
    reader = csv.reader(f)
    next(reader)
    data = []

    for row in reader:
        data.append(row)

    # data.pop(0)

# print(data)

# Read as a List, include headers

with open('numbers.csv') as f:
    reader = csv.reader(f)
    data = []

    for row in reader:
        data.append(row)

# print(data)

# Read as a Dict

with open('numbers.csv') as f:
    reader = csv.DictReader(f)
    data = []

    for row in reader:
        data.append(row)

# out = data[1]['col2']
# print(out)
