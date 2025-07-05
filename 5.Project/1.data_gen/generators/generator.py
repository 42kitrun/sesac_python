from abc import ABC, abstractmethod

# 중간 중계자를 통해서 처리하는 구조가 OOP 적인 설계
# 추상 클래스 - 필수로 구현해야 하는 함수를 지정 하였음
class Generator(ABC):
    registry = {}
    
    def __init_subclass__(cls, **kwargs):    # 나를 상속 받은 애들이 자동으로 실행하게 되는 함수
        super().__init_subclass__(**kwargs)
        Generator.registry[cls] = cls  # 그래서 나를 상속해간 놈들이 누군지 registry 에 기록함
    
    @abstractmethod
    def generate(self,*args):
        pass
    
class GenerateData:
    def __init__(self, cls, *count):
        if cls in Generator.registry:
            cls.generate(count)
        else:
            raise ValueError("내부에서 생성한 클래스가 아닙니다")