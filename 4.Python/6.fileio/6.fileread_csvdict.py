# https://docs.python.org/ko/3.13/library/csv.html
import csv

file_path = '4.Python/6.fileio/test.csv'
data = []

with open(file_path,'r', newline = '') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # print(row)
        data.append(row)

print(data)