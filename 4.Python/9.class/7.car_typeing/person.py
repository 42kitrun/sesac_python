class Person():
    def __init__(self,name:str, age:int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def set_name(self, name:str)->None:
        self._name = name

    @property
    def age(self)-> int:
        return self._age
    
    @age.setter
    def set_age(self, age:int)->None:
        if age >= 0:
            self._age = age
        else:
            print('나이는 0보다 커야 합니다.')
    
    def greet(self):    # 메소드(Method - 객체 함수)
        print(f'안녕하세요, 저의 이름은 {self._name}이고, 나이는 {self._age} 입니다.')

    def ride_car(self): # 메소드(Method - 객체 함수)
        print(f'자동차를 탑니다')