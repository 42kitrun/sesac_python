from db.crud import table_names
from abc import ABC

class Tables(ABC):
    _tables = None  # 클래스 변수로 선언

    @classmethod
    def get_tables(cls):
        if cls._tables is None:
            cls._tables = table_names()  # 처음 한 번만 실제로 DB에서 호출
        return cls._tables

    # def __init_subclass__(cls):    # 클래스를 "정의"하는 시점(≠ 인스턴스 생성 시)에만 실행
    #     super().__init_subclass__()
    #     if isinstance():
    def __init__(self, crud):
        # 타입 체크 내부 통일
        if not isinstance(crud, Crud):
            raise TypeError('User([crud class])() 이렇게 CRUD class를 입력하세요.')
        
        self.tables = self.get_tables()  # 모든 객체가 같은 값 사용
        self.crud = crud
        self.table = '' # 하위 클래스에서 정하기