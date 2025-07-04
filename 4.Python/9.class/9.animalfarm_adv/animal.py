from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self._name: str = name
        self._energy: int = 100
        self.sound = '' # 자식 클래스에서 재정의 지금은 그냥 기본값

    # @abstractmethod
    # def speak(self) -> None:
    #     pass
    def speak(self) -> None:
        print(f"{self._name} 은 {self.speak_style()} 라고 합니다.")
    
    def speak_style(self) -> str:
        if self._energy >= 80:
            return self.sound.upper()
        elif self._energy >= 50:
            return self.sound.capitalize()
        elif self._energy >= 20:
            return self.sound.lower()
        else:
            return "..."
    
    @abstractmethod # 상속받은 객체들이 꼭 가져야할 메소드
    def move(self) -> None:
        pass

    def feed(self, food: str) -> None:
        self._energy += 50
        print(f"{self._name} 은 {food} 를 먹었습니다. 잔여 에너지: {self._energy}")