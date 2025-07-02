from animal import Animal

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
        self._speak = 'Meow'
        self._shrink_energy = 5

    # 초중급까지는 잘 안씀
    def __str__(self): # 이 객체를 사람들이 보기 좋게 표현하는 함수
        return f'''Cat
          name : {self._name}
         speak : {self._speak}
        energy : {self._energy}'''

    def speak(self) -> None:
        print(self._speak)

    def move(self,count=1):
        if self._energy <= 0:
            print('에너지가 없습니다. 움직일 수 없습니다')
            return
        else:
            print(f'{self._name}이 {count}번 움직입니다. 에너지가 {self._shrink_energy*count} 감소합니다.')
            self._energy -= self._shrink_energy*count
            print(f'{self._name}의 에너지가 {self._energy} 남았습니다.')

    