from typing import Optional, List
from animal import Animal

class Farm:
    def __init__(self, name):
        print('농장을 만들었습니다')
        self._animals : List[Animal] = [] # 동물들 리스트를 담는 곳
        self._name: str = name

    def add_animals(self, animal:Animal)->list:
        self._animals.append(animal)
        print(f'{animal.name}을 농장에 추가했습니다')
        print(f'지금 농장에 {",".join([ani.name for ani in self._animals])}이/가 있습니다')
        return self._animals
    
    def feed_all(self, count=1) -> None:
        print('모든 동물들에게 밥을 줍니다.')
        for ani in self._animals:
            ani.set_energy = ani.energy + 50*count
            print(f'{ani.name}에게 밥을 주어 에너지가 50 증가되었습니다')
            print(f'{ani.name}의 에너지는 {ani.energy} 입니다')
        print('모든 동물들에게 밥을 주었습니다.')

    def play_all(self, count=1) -> None:
        print(f'모든 동물들과 {count}번 놀아줍니다.')
        for ani in self._animals:
            ani.set_energy = ani.energy -10*count
            print(f'{ani.name}과 놀아 주어 에너지가 {10*count} 감소되었습니다')
            print(f'{ani.name}의 에너지는 {ani.energy} 입니다')
        print('모든 동물들과 놀아주었습니다.')

    def show_all(self, animal: Optional[Animal]=None ) -> None:
        if animal is None:
            for ani in self._animals:
                print(ani)
        else:
             print(animal)