# 241
import datetime
print(datetime.datetime.now())
print('-'*30, 241)

# 242
print(type(datetime.datetime.now()))
print('-'*30, 242)

# 243
#datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
print(f'5일전 : {datetime.datetime.today() - datetime.timedelta(5)}')
print(f'4일전 : {datetime.datetime.today() - datetime.timedelta(4)}')
print(f'3일전 : {datetime.datetime.today() - datetime.timedelta(3)}')
print(f'2일전 : {datetime.datetime.today() - datetime.timedelta(2)}')
print(f'1일전 : {datetime.datetime.today() - datetime.timedelta(1)}')
print('-'*30, 243)

# 244
#18:35:01 
print( datetime.datetime.now().strftime('%H:%M:%S'))
print('-'*30, 244)

# 245
print(datetime.datetime.strptime("2020-05-04",'%Y-%m-%d'))
print('-'*30, 245)

# 246
from time import sleep

while False :
    print(datetime.datetime.now())
    sleep(1)

print('-'*30, 246)

# 247
print('모듈을 import하는 4가지 방법')
print('''
1 : import module_name
2 : import 모듈 as 별칭
3 : from 모듈 import 이름
4 : from 모듈 import''')
print('-'*30, 247)

# 248
import os
print(os.getcwd())
print('-'*30, 248)

# 249
# os.rename('/Users/seSAC/Desktop/file.txt','/Users/seSAC/Desktop/new_file.txt')
print('-'*30, 249)

# 250
# 0.0 부터 5.0까지 0.1씩 증가하는 값
import numpy as np
print(np.arange(0,5.1,0.1))
print('-'*30, 250)