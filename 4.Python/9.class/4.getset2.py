class Person:
    # 초중급 에서도 필수
    def __init__(self, name, age):
        self.__name = name  # 속성 (Attribute) - __ 밑줄 두개는 private 속성이라서, 클래서 밖에서 접근 불가
        self.__age = age   # 속성 (Attribute)  - 개별 데이터를 저장하는 공간

    # getter, setter 내부 변수에 저장해서 값을 읽어올때는 getter를 사용하고 get_name()
    # 내부 변수에 셋팅을 할때는 set_name()

    @property # 이 함수는 getter 입니다.
    def name(self):
        return self.__name
    
    @name.setter  # 이 함수는 name의 setter 입니다.
    def name(self,name:str):
        self.__name = name

    @property # 이 함수는 getter 입니다.
    def age(self):
        return self.__age
    
    @age.setter # 이 함수는 age의 setter 입니다.
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("나이는 0보다 커야 합니다.")

    def greet(self):    # 메소드(Method - 객체 함수)
        print(f'안녕하세요, 저는 {self.name}입니다.')

    def ride_car(self): # 메소드(Method - 객체 함수)
        print(f'자동차를 탑니다')

person1 = Person('김철수',30) # (객체) instance
person2 = Person('홍길동',25)

# setter/getter를 파이선 신버전에서 decorator로 지정을 했으면,
# 함수가 아닌 변수처럼 쉽게 접근할 수 있음
print(person1.age)

person1.name = "박철수"
person1.age = 35

print(person1.age)

person1.age = -10

# 이 최신 파이썬 문법으로 짜면?? 객체 안에 변수를 자유롭게 바꾸는 것처럼 보이지만,
# 실제로는 함수를 통해서, 에러 처리 등등을 통과해서 할당되는 매~우 재밌는(?) 구조임.