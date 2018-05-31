import csv

cols_array = [[1, 2, 3], [4, 5, 6]]

f = open('numbers.csv', 'w')

with f:

    writer = csv.writer(f)

    for row in cols_array:
        writer.writerow(row)
