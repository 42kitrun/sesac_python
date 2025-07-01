## 3.1.1 연습 문제: 자릿수를 구하는 함수 만들기
def numOfDigits(num:int):
    if num > 0:
        return len(list(str(round(num))))

# print(numOfDigits(12345))

## 3.1.2 연습 문제: 구구단
# for n in range(2,10):
#     for m in range(1,10):
        # print(f'{n} * {m} = {n*m}')

## 3.2.1 연습 문제: 숫자 읽기 함수(1~10)
def korean_number(num:int):
    return [0,'일','이','삼','사','오','육','칠','팔','구','십'][num]

# print(korean_number(10))

## 3.2.2 연습 문제: 함수 정의하기
# 문제 1
def triple(x):
    return x*3

# 문제 2
from datetime import datetime

def korean_age(year:int):
    assert year <= 9999

    print(datetime.today().year - year+1)

# korean_age(2004)

## 3.2.3 연습 문제: 이자(단리) 계산
# 문제1
def simple_interest(p:float,r:float,t:float):
    return p*r*t
# print(simple_interest(10_000_000, 0.03875, 5))

# 문제2
def simple_interest_amount(p:float,r:float,t:float):
    return p*(1+ r*t)

print(simple_interest_amount(10_000_000, 0.03875, 5))