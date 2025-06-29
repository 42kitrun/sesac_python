# 251
print('''클래스는 클래스는 일종의 설계도로, 하나의 타입을 정의하는 방법입니다. 클래스에는 관련있는 데이터와 함수를 한 데 모아 정의할 수 있습니다
객체는 클래스로 만들어진 결과물''')
print('-'*30, 251)

# 252
class Human:
    pass
print('-'*30, 252)

# 253
areum = Human()
print('-'*30, 253)

# 254
class Human:
    def __init__(self):
        print("응애응애")

areum = Human()
print('-'*30, 254)

# 255
class Human:
    def __init__(self,name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
print(areum.name,areum.age,areum.sex)
print('-'*30, 255)

# 256
# 이름: 조아름, 나이: 25, 성별: 여자
print(f'이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}')
print('-'*30, 256)

# 257
class Human:
    def __init__(self,name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
       print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')

areum = Human("아름", 25, "여자")
areum.who()
# 여러 객체가 같은 클래스에서 만들어져도,
# 각 객체의 데이터를 구분해서 다룰 수 있도록 하기 위해
# 파이썬이 자동으로 self를 넘겨주는 것
print('-'*30, 257)

# 258
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
       print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')
    
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("모름", 0, "모름")
print(f'이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}')
areum.setInfo("아름", 25, "여자")
print(f'이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}')
print('-'*30, 258)

# 259
class Human:
    # 모든 Human class에 동일하게 적용되는 속성
    sleepingHours  = 8

    # 각 객체별 속성을 다르게 할 수 있다
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 클래스로 만든 객체(인스턴스)는 각각 고유한 데이터(속성)를 가질 수 있습니다.
    # 메서드를 호출할 때, 파이썬은 그 메서드가 어느 인스턴스에 속하는지 알아야, 그 인스턴스의 데이터에 접근할 수 있습니다.
    # 메서드 호출 방식 원리
    # 인스턴스에서 메서드를 호출하면 (aruem.who()),
    # 파이썬은 내부적으로 클래스이름.메서드(인스턴스, ...)형태(aruem.who(aruem))로 바꿔서 실행합니다.
    # python이 첫 번째 인자로 self(즉, 인스턴스 자기 자신)를 자동으로 넘겨주는 이유는
    # 메서드가 어떤 객체(인스턴스)의 데이터와 기능을 다루는지 명확하게 구분하기 위함입니다.

    def who(self):
       print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')
    
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def __del__(self): # class 소멸
        print(f"나의 죽음을 알리지 마라")

areum = Human("아름", 25, "여자")
del areum
print('-'*30, 259)
# 260
# 만약 self를 넣지 않고 메서드를 정의하면, 파이썬이 인스턴스를 넘겨주려고 하는데 받을 인자가 없어서 에러가 발생합니다.
class OMG :
    def print(self) :
        print("Oh my god")


mystock = OMG()
mystock.print()      # OMG.print(mystock)
print('-'*30, 260)

# 261
class Stock:
    pass
print('-'*30, 261)

# 262
class Stock:
    def __init__(self, stock_name,code ):
        self.name = stock_name
        self.code = code

삼성 = Stock("삼성전자", "005930")
print('-'*30, 262)

# 263
class Stock:
    def __init__(self, stock_name,code ):
        self.name = stock_name
        self.code = code
    def set_name(self, name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자") # Stock.set_name(a, "삼성전자")
print('-'*30, 263)

# 264
class Stock:
    def __init__(self, stock_name,code ):
        self.name = stock_name
        self.code = code
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code        

a = Stock(None, None)
a.set_code("005930")
print('-'*30, 264)

# 265
class Stock:
    def __init__(self, stock_name,code ):
        self.name = stock_name
        self.code = code
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        print('name :', self.name)
        return self.name
    def get_code(self):
        print('code :', self.code)
        return self.code

삼성 = Stock("삼성전자", "005930")
삼성.get_name()
삼성.get_code()
print('-'*30, 265)

# 266
# 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요
class Stock:
    def __init__(self, stock_name,code, per, pbr, dividend):
        self.name = stock_name
        self.code = code
        if((type(per) == float) and (type(pbr) == float) and (type(dividend) == float)):
            pass
        else:
            raise ValueError('per,BER,dividend must be float!')
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        print('name :', self.name)
        return self.name
    def get_code(self):
        print('code :', self.code)
        return self.code
print('-'*30, 266)

# 267
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print('-'*30, 267)

# 268
# set_per, set_pbr, set_dividend 
class Stock:
    def __init__(self, stock_name,code, per, pbr, dividend):
        self.name = stock_name
        self.code = code
        if((type(per) == float) and (type(pbr) == float) and (type(dividend) == float)):
            pass
        else:
            raise ValueError('per,BER,dividend must be float!')
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def set_per(self, per):
        self.per = per
    def set_pbr(self, pbr):
        self.pbr = pbr
    def set_dividend(self, dividend):
        self.dividend = dividend

    def get_name(self):
        print('name :', self.name)
        return self.name
    def get_code(self):
        print('code :', self.code)
        return self.code
print('-'*30, 268)

# 269
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print('변경전 :',삼성.per)
삼성.set_per(12.75)
print('변경후 :',삼성.per)
print('-'*30, 269)

# 270
for c in [ Stock('삼성전자','005930',15.79,1.33,2.83)
, Stock('현대차','005380',8.70,0.35,4.27)
,Stock('LG전자','066570',317.34,0.69,1.37)]:
    print(f'{c.name} code : {c.code} per : {c.per}')
print('-'*30, 270)

# 271
# 은행이름, 예금주, 계좌번호, 잔액
import random
class Account:
    def __init__(self, name, balance):
        self.bank = 'SC은행'
        self.name = name
        self.account_number = f'{str(random.randrange(999)):0>3}-{str(random.randrange(99)):0>2}-{str(random.randrange(999999)):0>6}'
        self.balance = balance
    
kim = Account("김민수", 100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)
print('-'*30, 271)

# 272
import random
class Account:
    # 인스턴스 갯수
    # class variable
    account_count  = 0

    def __init__(self, name, balance):
        self.bank = 'SC은행'
        self.name = name
        self.account_number = f'{str(random.randrange(999)):0>3}-{str(random.randrange(99)):0>2}-{str(random.randrange(999999)):0>6}'
        self.balance = balance
        Account.account_count += 1

kim = Account("김민수", 100)
print(Account.account_count)
lee = Account("이민수", 100)
print(Account.account_count)
print('-'*30, 272)

# 273
# get_account_num() 
import random
class Account:
    # 인스턴스 갯수
    # class variable
    account_count  = 0

    def __init__(self, name, balance):
        self.bank = 'SC은행'
        self.name = name
        self.account_number = f'{str(random.randrange(999)):0>3}-{str(random.randrange(99)):0>2}-{str(random.randrange(999999)):0>6}'
        self.balance = balance
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count) 
        return cls.account_count

kim = Account("김민수", 100)
lee = Account("이민수", 100)
kim.get_account_num()    
print('-'*30, 273)

# 274
import random
class Account:
    # 인스턴스 갯수
    # class variable
    account_count  = 0

    def __init__(self, name, balance):
        self.bank = 'SC은행'
        self.name = name
        self.account_number = f'{str(random.randrange(999)):0>3}-{str(random.randrange(99)):0>2}-{str(random.randrange(999999)):0>6}'
        self.balance = balance
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count) 
        return cls.account_count
    
    def deposit(self,deposits):
        if(deposits >= 1):
            self.balance += deposits
print('-'*30, 274)

# 275
# withdraw
import random
class Account:
    # 인스턴스 갯수
    # class variable
    account_count  = 0

    def __init__(self, name, balance):
        self.bank = 'SC은행'
        self.name = name
        self.account_number = f'{str(random.randrange(999)):0>3}-{str(random.randrange(99)):0>2}-{str(random.randrange(999999)):0>6}'
        self.balance = balance
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count) 
        return cls.account_count
    
    def deposit(self,deposits):
        if(deposits >= 1):
            self.balance += deposits
        print(self.balance)

    def withdraw(self, withdraw):
        if(self.balance >= withdraw):
            self.balance -= withdraw

k = Account("kim", 100)
k.deposit(100)
k.withdraw(90)
print(k.balance)
print('-'*30, 275)

# 276
# display_info() 
import random
class Account:
    # 인스턴스 갯수
    # class variable
    account_count  = 0

    def __init__(self, name, balance):
        self.bank = 'SC은행'
        self.name = name
        self.account_number = f'{str(random.randrange(999)):0>3}-{str(random.randrange(99)):0>2}-{str(random.randrange(999999)):0>6}'
        self.balance = balance
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count) 
        return cls.account_count
    
    def deposit(self,deposits):
        if(deposits >= 1):
            self.balance += deposits
            print(self.balance)
            return self.balance

    def withdraw(self, withdraw):
        if(self.balance >= withdraw):
            self.balance -= withdraw
            print(self.balance)
            return self.balance

    def display_info(self):
        # amount = list(str(self.balance))
        print(f'''은행이름: {self.bank}
예금주: {self.name}
계좌번호: {self.account_number}
잔고: {f'{self.balance:,}'}원''') # f-string 내장된 포맷
# 잔고: {''.join([','+n if len(amount) % 3 == i % 3 else n for i,n in enumerate(amount)])}원''') 

p = Account("파이썬", 10000)
p.display_info()
print('-'*30, 276)

# 277
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경
import random
class Account:
    # 인스턴스 갯수
    # class variable
    account_count  = 0

    def __init__(self, name, balance):
        self.deposit_count = 0

        self.bank = 'SC은행'
        self.name = name
        self.account_number = f'{str(random.randrange(999)):0>3}-{str(random.randrange(99)):0>2}-{str(random.randrange(999999)):0>6}'
        self.balance = balance
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count) 
        return cls.account_count
    

    def deposit(self,deposits):
        if(deposits >= 1):
            self.balance += deposits
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance += self.balance * 0.01
            print(self.balance)
            return self.balance

    def withdraw(self, withdraw):
        if(self.balance >= withdraw):
            self.balance -= withdraw

            print(self.balance)
            return self.balance

    def display_info(self):
        print(f'''은행이름: {self.bank}
예금주: {self.name}
계좌번호: {self.account_number}
잔고: {f'{self.balance:,}'}원''') # f-string 내장된 포맷

p = Account("파이썬", 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)
print('-'*30, 277)

# 278
import random
class Account:
    # 인스턴스 갯수
    # class variable
    account_count  = 0

    def __init__(self, name, balance):
        self.deposit_count = 0

        self.bank = 'SC은행'
        self.name = name
        self.account_number = f'{str(random.randrange(999)):0>3}-{str(random.randrange(99)):0>2}-{str(random.randrange(999999)):0>6}'
        self.balance = balance
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count) 
        return cls.account_count
    

    def deposit(self,deposits):
        if(deposits >= 1):
            self.balance += deposits
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance += self.balance * 0.01
            print(self.balance)
            return self.balance

    def withdraw(self, withdraw):
        if(self.balance >= withdraw):
            self.balance -= withdraw

            print(self.balance)
            return self.balance

    def display_info(self):
        print(f'''은행이름: {self.bank}
예금주: {self.name}
계좌번호: {self.account_number}
잔고: {f'{self.balance:,}'}원''') # f-string 내장된 포맷
        
client = [Account("KIM", 10000000)
,Account("LEE", 10000)
,Account("PARK", 10000)]
print('-'*30, 278)

# 279
print([c.display_info() for c in client if c.balance >= 1000000])
print('-'*30, 279)

# 280
# 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.
import random
from datetime import datetime as dt

class Account:
    # 인스턴스 갯수
    # class variable
    account_count  = 0

    def __init__(self, name, balance):
        self.deposit_count = 0

        self.bank = 'SC은행'
        self.name = name
        self.account_number = f'{str(random.randrange(999)):0>3}-{str(random.randrange(99)):0>2}-{str(random.randrange(999999)):0>6}'
        self.balance = balance
        Account.account_count += 1

        self.deposit_log = f'deposit_history\n[{dt.now().date()}] 입금 : {self.balance}원 / 계좌 생성\n'
        self.withdraw_log = 'withdraw_history\n'

    @classmethod
    def get_account_num(cls):
        print(cls.account_count) 
        return cls.account_count
    

    def deposit(self,deposits):
        if(deposits >= 1):
            self.balance += deposits
            self.deposit_count += 1
            self.deposit_log += f'[{dt.now().date()}] 입금 : {deposits}원 / 잔액 : {self.balance}\n'
            if self.deposit_count % 5 == 0:
                self.deposit_log += f'[{dt.now().date()}] 이자 : {self.balance * 0.01}원 / 잔액 : {self.balance}\n'
                self.balance += self.balance * 0.01
            print(self.balance)
            return self.balance

    def withdraw(self, withdraw):
        if(self.balance >= withdraw):
            self.balance -= withdraw
            self.withdraw_log += f'[{dt.now().date()}] 출금 : {withdraw}원 / 잔액 : {self.balance}\n'
            print(self.balance)
            return self.balance

    def display_info(self):
        print(f'''은행이름: {self.bank}
예금주: {self.name}
계좌번호: {self.account_number}
잔고: {f'{self.balance:,}'}원''') # f-string 내장된 포맷
    
    def deposit_history(self):
        print(self.deposit_log)
        return self.deposit_log

    def withdraw_history(self):
        print(self.withdraw_log)
        return self.withdraw_log
    
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()
print('-'*30, 280)

# 281
class 차:
    def __init__(self,바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

car = 차(2, 1000)
print('car.바퀴',car.바퀴)
print('car.가격',car.가격)
print('-'*30, 281)

# 282
class 차:
    def __init__(self,바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    pass
print('-'*30, 282)

# 283
class 차:
    def __init__(self,바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    pass

bicycle = 자전차(2, 100)
print('bicycle.바퀴',bicycle.바퀴)
print('bicycle.가격',bicycle.가격)
print('-'*30, 283)

# 284
class 차:
    def __init__(self,바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    def __init__(self, 바퀴, 가격,구동계):
        super().__init__(바퀴, 가격)  # 부모 클래스의 __init__ 호출
        self.구동계 = 구동계           # 자식 클래스만의 속성 추가

bicycle = 자전차(2, 100, "시마노")
print(bicycle.구동계)
print('-'*30, 284)

# 285
class 차:
    def __init__(self,바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    def __init__(self, 바퀴, 가격,구동계):
        super().__init__(바퀴, 가격)  # 부모 클래스의 __init__ 호출
        self.구동계 = 구동계           # 자식 클래스만의 속성 추가

class 자동차(차):
    # def __init__(self, 바퀴, 가격):
    #     super().__init__(바퀴, 가격)

    def 정보(self):
        print(f'바퀴수 {self.바퀴}')
        print(f'가격 {self.가격}')

car = 자동차(4, 1000)
car.정보()
print('-'*30, 285)

# 286
class 차:
    def __init__(self,바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print(f'바퀴수 {self.바퀴}')
        print(f'가격 {self.가격}')

class 자전차(차):
    def __init__(self, 바퀴, 가격,구동계):
        super().__init__(바퀴, 가격)  # 부모 클래스의 __init__ 호출
        self.구동계 = 구동계           # 자식 클래스만의 속성 추가

class 자동차(차):
    # def __init__(self, 바퀴, 가격):
    #     super().__init__(바퀴, 가격)

    def 정보(self):
        print(f'바퀴수 {self.바퀴}')
        print(f'가격 {self.가격}')

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()
print('-'*30, 286)

# 287
class 차:
    def __init__(self,바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print(f'바퀴수 {self.바퀴}')
        print(f'가격 {self.가격}')

class 자전차(차):
    def __init__(self, 바퀴, 가격,구동계):
        super().__init__(바퀴, 가격)  # 부모 클래스의 __init__ 호출
        self.구동계 = 구동계           # 자식 클래스만의 속성 추가
    
    def 정보(self):
        super().정보()              # 부모 클래스의 __init__ 호출
        print(f'구동계 {self.구동계}')# 자식 클래스만의 속성 추가

class 자동차(차):
    pass

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()
print('-'*30, 287)

# 288
class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()
print('-'*30, 288)

# 289
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")

나 = 자식()
print('-'*30, 289)

# 290
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()
print('-'*30, 290)
