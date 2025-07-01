## 5.2.1 연습 문제: 모듈 사용법 알아내기
# 문제1
import calendar

dir(calendar)

# 문제2
[x for x in dir(calendar) if 'leap' in x]

# 문제3
# help(calendar.isleap)

# 문제4
calendar.isleap(2077)

## 5.2.2 연습 문제: 직각삼각형의 빗변 길이 구하기
# 문제 1
import math

a=3
b=4
c = math.sqrt(a**2+b**2)
print(c)

# 문제 2
def hypotenuse(a:float,b:float)->float:
    return math.sqrt(a**2+b**2)

## 5.2.3 연습 문제: calendar와 tkinter
# 1. calendar
import calendar

c= calendar.TextCalendar()
m = c.formatmonth(2021,2)
print(m)

# 2. tkinter
import tkinter as tk

s = "Life is short\nUse Python"

# root = tk.Tk()
# t = tk.Text(root, height=2, width=15)
# t.insert(tk.END, s)
# t.pack()
# tk.mainloop()

# 3. calendar와 tkinter

c= calendar.TextCalendar().formatmonth(2021,3)
# root = tk.Tk()
# t = tk.Text(root, height=7, width=20)
# t.insert(tk.END, c)
# t.pack()
# tk.mainloop()

## 5.3.2 연습 문제: 밴드 이름 짓기 (1)
import random

color = ('땡땡이', '베이지', '블랙', '블루', '회색', '청색', '레드', '파란', '핑크', '그레이', '베이지', '화이트', '청', '초록', '회색', '노랑', '인디안 핑크', '차콜', '브라운', '검은', '분홍')
food = ('소라과자', '아이스 바닐라 라떼', '소보로', '쭈꾸미', '요거트 아이스크림', '오란다', '와플', '아이스티', '로제 떡볶이', '스트로베리', '커피', '진라면', '초코퍼지', '닭갈비', '크래커', '맥스봉', '라떼', '참외', '소시지', '햄버거', '콰삭칩', '된찌', '오렌지', '옹심이', '아메리카노')

color_index = random.randint(0,len(color))
food_index = random.randint(0,len(food))

print(f'{color[color_index]} {food[food_index]}')