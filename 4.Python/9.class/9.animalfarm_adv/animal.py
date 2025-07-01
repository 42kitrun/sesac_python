from abc import ABC, abstractmethod

class Animal:
    sound =''

    def __init__(self, name: str) -> None:
        self._name = name
        self._energy:int = 100
        self._speak = ''
        self._move = 0

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def set_name(self,name:str)->None:
        self._name = name

    @property
    def energy(self) -> int:
        return self._energy
    
    @energy.setter
    def set_energy(self,energy:int)->None:
        self._energy = energy

    # @abstractmethod
    # def speak(self):
    #     pass

    def speak(self) -> None:
        print(f'{self._name}은 {self.speak_style()} 라고 합니다')

    @abstractmethod
    def move(self):
        pass

    def speak_style(self) -> str:
        if self._energy >= 80:
            return self.sound.upper()