from abc import ABC, abstractmethod

# 중간 중계자를 통해서 처리하는 구조가 OOP 적인 설계
# 추상 클래스 - 필수로 구현해야 하는 함수를 지정 하였음
class Generator(ABC):
    registry = {}
    
    def __init_subclass__(cls):    # 나를 상속 받은 애들이 자동으로 실행하게 되는 함수
        super().__init_subclass__()
        Generator.registry[cls] = cls  # 그래서 나를 상속해간 놈들이 누군지 registry 에 기록함
    
class GenerateData:
    def __init__(self, generator, count=None):
        self.generator = generator
        self.count = count

    def __call__(self): # GenerateData(generator,count)()<- 오른쪽에 ()를 붙여야 call
        # count가 없으면 generator.generate()만 호출
        if self.count is None:
            return self.generator.generate()
        # count가 있으면 generator.generate(count) 호출
        else:
            return self.generator.generate(self.count)
        
        f'''if cls in Generator.registry:
            cls.generate(*count)
        else:
            raise ValueError("내부에서 생성한 클래스가 아닙니다")'''
