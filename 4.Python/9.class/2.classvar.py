class Person():
    __count=0 # 클래스 변수 (공통, 공용, 영역에 해당함)
    ''' 밑줄 1개 _ (네임맹글링) : protected 클래스 밖에서 접근 가능
        밑줄 2개 __ (네임맹글링) : private 클래스 밖에서 접근 불가
        파이썬에서 클래스 내부에서만 사용하려는 변수(속성)나 메서드를 만들 때,
        이름 앞에 **밑줄 두 개(__)**를 붙여서 사용합니다.

        이렇게 하면, 외부에서 직접 접근하는 것을 어렵게 만듭니다.

        파이썬은 이 변수나 메서드의 이름을 자동으로 바꿔서(맹글링),
        의도치 않은 접근을 막아줍니다.

        예)
        __secret → _MyClass__secret
        self.__name → self._MyClass__name

        ## 왜 이렇게 할까요?
        - 클래스 내부에서만 사용하는 변수/메서드임을 명확히 하기 위해서.
        - 의도치 않은 외부 접근을 막기 위해서.
        - 상속받은 클래스에서 이름이 겹치는 것을 방지하기 위해서.
    '''

    # 초중급에서도 필수
    def __init__(self, name, age):
        self.name = name # 속성(attribute) - 개별 데이터를 저장하는 공간
        self.age = age   # 속성(attribute)
        self._count = 1  # 개체의 count 변수
        Person.__count += 1 # 클래스 변수에 접근해서 1을 증가한다
        # 클래스 내부에서는 Person.__count로 접근해도 네임 맹글링이 적용되어 정상 동작합니다.   

    def greet(self):    # 메소드(Method - 객체 함수)
        print(f'안녕하세요, 저는 {self.name}입니다.')

    def ride_car(self): # 메소드(Method - 객체 함수)
        print(f'자동차를 탑니다')

    # getter, setter 내부 변수에 저장해서 값을 읽어올때는 getter를 사용하고 get_name()
    # 내부 변수에 셋팅을 할때는 set_name()
    @classmethod # class 변수에 접근 가능하도록 나의 함수에 기능을 더해줌 - 데코레이터
    def get_count(cls): # 클래스 자체에 접근하기 위해서 cls 라는 클래스 자신을 칭하는 변수를 받아옴
        return cls.__count
    
    # @classmethod
    # def set_count(cls, count):
    #     cls.count = count

# 객체를 찍어내는 과정 = 실체화  =instantiation : 설계도(클래스)를 바탕으로 실제 객체(인스턴스)를 생성하는 행위
person1 = Person('김철수',30) # (객체) instance
# print(f'만들어진 사람수: {person1.__count}') # 밑줄 2개는 접근 불가
person2 = Person('홍길동',25)
print(f'만들어진 사람수: {person1._count}') # 밑줄 1개는 접근가능
print(f'만들어진 사람수: {person2._count}')

# person1 = {
#     'name': '김철수'
#     , 'age':30
#     , '__class__':Person
#     , '__dict__':{'name': '김철수', 'age':30}
# }

print(person1.name)
print(person1.age)
print(person1.__class__)
print(person1.__dict__)

# 파이썬에서 변수 이름 앞에 __(밑줄 두 개)를 붙이면
# **네임 맹글링(name mangling)**이 일어나서
# 실제 변수명이 _클래스명__변수명으로 바뀝니다.
# print(Person.__count)  # 에러! (AttributeError)
# print(Person._Person__count)  # private 클래스 밖에서 접근 불가