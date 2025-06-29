# 201
def print_coin() :
    print('비트코인')
print('-'*30, 201)

# 202
print_coin()
print('-'*30, 202)

# 203
for i in range(100):
    print_coin()
print('-'*30, 203)

# 204
def print_coins():
    print(f'{len([print_coin() for i in range(100)])}번 출력 완료')

print_coins()
print('-'*30, 204)

# 205
# 인터프리터 언어는 위에서 부터 읽기 때문에 정의하고 호출한다
def hello():
    print("Hi")

hello()
print('-'*30, 205)

# 206
def message() :
    print("A")
    print("B")

message()
print("C")
message()
print('-'*30, 206)

# 207
print("A")

def message() :
    print("B")

print("C")
message()
print('-'*30, 207)


# 208
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()
print('-'*30, 208)

# 209
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()
print('-'*30, 209)

# 210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
print('-'*30, 210)

# 211
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")
print('-'*30, 211)

# 212
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)
print('-'*30, 212)



# 213
# 인수가 있어야하는데 없어요. 넣어주세요
def 함수(문자열) :
    print(문자열)

함수('Hello World')
print('-'*30, 213)

# 214
# 문자와 숫자를 더할 수 없어요
def 함수(a, b) :
    print(a + b)

함수("안녕", '3')
print('-'*30, 214)

# 215
def print_with_smile(string_arg):
        print(f'{string_arg} :D')
    
print_with_smile('e')    
print('-'*30, 215)

# 216
print_with_smile('안녕하세요')
print('-'*30, 216)

# 217
def print_upper_price(price):
    print(round(price *0.7), 'is upper price(30%)')

print_upper_price(10000)
print('-'*30, 217)

# 218
def print_sum (a,b):
    print(a +b)

print_sum(2,3)
print('-'*30, 218)

# 219
def print_arithmetic_operation(a,b):
    print(f'''
{a} + {b} : {a+b}
{a} - {b} : {a-b}
{a} * {b} : {a*b}
{a} / {b} : {round(a/b,2)}''')
    
print_arithmetic_operation(3,4)
print('-'*30, 219)

# 220
def print_max(a,b,c):
    max = 0
    if a>=b:
        max = a
    else:
        max=b
    if max >= c:
        print(max)
    else:
        print(c)

print_max(1,2,3)
print('-'*30, 220)

# 221
def print_reverse(string):
    print(string[::-1])
    # print(''.join([list(string)[i] for i in range(len(string)-1,-1,-1)]))

print_reverse("python")
print('-'*30, 221)

# 222
def print_score(array_score):
    # average = 0
    # for n in array_score:
    #     average += n
    
    print(round(sum(array_score)/len(array_score),2))

print_score ([1, 2, 3])
print('-'*30, 222)

# 223
def print_even(array_arg):
    print([n for n in array_arg if n % 2 == 0])

print_even ([1, 3, 2, 10, 12, 11, 15])
print('-'*30, 223)

# 224
def print_keys(dic):
    print(dic.keys())

print_keys ({"이름":"김말똥", "나이":30, "성별":0})
print('-'*30, 224)

# 225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(dic,str_key):
    print(dic[str_key])

print_value_by_key  (my_dict, "10/26")
print('-'*30, 225)

# 226
def print_5xn(string):
    for i in range(0,len(string),5):
        print(string[i:i+5])

print_5xn("아이엠어보이유알어걸")

print('-'*30, 226)

# 227
def printmxn(string, num):
    for i in range(0,len(string),num):
        print(string[i:i+num])

printmxn("아이엠어보이유알어걸", 3)
print('-'*30, 227)

# 228
def calc_monthly_salary(salary):
    print(int(salary/12))

calc_monthly_salary(12000000)
print('-'*30, 228)

# 229
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)
print('-'*30, 229)

# 230
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)
print('-'*30, 230)

# 231
# result는 지역변수이므로 함수 밖에서는 정의 되지 않았다.
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
# print (result)
print('-'*30, 231)

# 232
def make_url(name):
    return f'www.{name}.com'

print(make_url("naver"))
print('-'*30, 232)

# 233
def make_list(string):
    return(list(string))

print(make_list("abcd"))
print('-'*30, 233)

# 234
def pickup_even(arry_num):
    return[n for n in arry_num if n %2 ==0]

print(pickup_even([3, 4, 5, 6, 7, 8]))
print('-'*30, 234)

# 235
def convert_int(str_num):
    return str_num.replace(',','')

print(convert_int("1,234,567"))

print('-'*30, 235)

# 236
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)
print('-'*30, 236)

# 237
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)
print('-'*30, 237)

# 238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)
print('-'*30, 238)

# 239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)
print('-'*30, 239)

# 240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
print('-'*30, 240)