from db.tables import Tables
from abc import ABC,abstractmethod

class Crud(ABC):

    def __init__(self, tables):
        # 타입 체크 내부 통일
        if not isinstance(tables, Tables):
            raise TypeError('Get(User())() 이렇게 Crud class를 입력하세요.')
        self.tables = tables.sql()

    def __call__(self):
        return self.execute()

    @abstractmethod
    def execute(self):
        pass
    
    # cursor 결과를 dict로 변환
    @staticmethod
    def dict_r(cursor):
        columns = [col[0].lower() for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]