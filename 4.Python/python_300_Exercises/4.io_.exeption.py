# 291
with open('/Users/seSAC/Desktop/매수종목1.txt', 'w',encoding="utf-8") as f: 
    f.write('''005930
005380
035420''')
    
with open('/Users/seSAC/Desktop/매수종목1.txt', 'r') as f: 
    print(f.read())
print('-'*30, 291)

# 292
with open('/Users/seSAC/Desktop/매수종목2.txt', 'w',encoding="utf-8") as f: 
    f.write('''005930 삼성전자
005380 현대차
035420 NAVER''')

with open('/Users/seSAC/Desktop/매수종목2.txt', 'r') as f: 
    print(f.read())
print('-'*30, 292)

# 293
import csv

with open('/Users/seSAC/Desktop/매수종목.csv', 'w', encoding='cp949') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['종목명', '종목코드', 'PER'])
    writer.writerow(['삼성전자', '005930', 15.79])
    writer.writerow(['NAVER', '035420', 55.82])

with open('/Users/seSAC/Desktop/매수종목.csv', 'r', encoding='cp949') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
print('-'*30, 293)

# 294
with open('/Users/seSAC/Desktop/매수종목1.txt', 'r') as f: 
    print([row.strip() for row in f.readlines()])
print('-'*30, 294)

# 295
with open('/Users/seSAC/Desktop/매수종목2.txt', 'r') as f: 
    print({row.strip().split()[0] :row.strip().split()[1] for row in f.readlines()})
print('-'*30, 295)

# 296
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(float(0))
print('-'*30, 296)

# 297
li = []
per = ["10.31", "", "8.00"]

for i in per:
    try:
        li += [float(i)]
    except:
        li += [0]

print(li)
print('-'*30, 297)

# 298
try:
    a = 3/0
except ZeroDivisionError:
    print("0으로 나누면 안되요")
print('-'*30, 298)

# 299
data = [1, 2, 3]
for i in range(5):
    try:
    
        print(data[i])
    except IndexError as i:
        print(i)
print('-'*30, 299)

# 300
per = ["10.31", "", "8.00"]
for i in per:
    try:
        print(float(i))
    except:
        print(f'"{i}"isnt float so, convert into 0')
        print(0)
    else:
        print(i,'is float')
    finally:
        print(f'converting "{i}" is finished!]')
print('-'*30, 300)