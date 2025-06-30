# https://docs.python.org/ko/3.13/library/csv.html
# csv 파일은?? comma seperated value
import csv

file_path = '4.Python/6.fileio/test.csv'

data=[
    ['Name','Age','City'],
    ['John',25,'Seoul'],
    ['Jane',30,'Busan'],
    ['Bob',35,'Jeju']
    ]

print(data)
for i in range(len(data)):
    print(data[i])

with open(file_path,'w', newline = '') as file:
    csv_writer = csv.writer(file)
    
    csv_writer.writerows(data)
    csv_writer.writerow(['Alice',40,'Suwon'])

print('CSV 쓰기 완료')