# https://docs.python.org/ko/3.13/library/csv.html
import csv

file_path = '4.Python/6.fileio/test.csv'

data=[
    {'Name':'John','Age':25,'City':'Seoul'},
    {'Name':'Jane','Age':30,'City':'Busan'},
    {'Name':'Bob','Age':35,'City':'Jeju'}
   ]

print(data)
for person in data:
    print(f'사람의 이름은 {person["Name"]} 및 나이는 {person["Age"]}')
    # for key, value in person.items():
    #     print(f'Key: {key}, Value: {value}')

with open(file_path,'w', newline = '') as file:
    headers = ['Name','Age']
    headers = data[0].keys() # headers = ['Name','Age','City']
    csv_writer = csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    
    csv_writer.writerows(data)
print('CSV 쓰기 완료')