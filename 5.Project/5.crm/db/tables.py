from db.oracle import *
from abc import ABC

class Tables(ABC):
    _tables = None  # 클래스 변수로 선언
    
    # def __init_subclass__(cls):    # 클래스를 "정의"하는 시점(≠ 인스턴스 생성 시)에만 실행
    #     super().__init_subclass__()
    #     if isinstance():
    def __init__(self):
        self.tables = Tables.get_tables()  # 모든 객체가 같은 값 사용
        self.table = '' # 하위 클래스에서 정하기

    def __repr__(self):
        return '''
            User( *attr=('paging',), **kwargs)
            User(paging=[list_cnt, start_rownum])
            예) User(paging=[20, 80]) (0 이 시작) 80번째 데이터부터 20개
            예) User(name, gender, name = ('차은우','이지은'), gender = 'female')
            예) User(paging, name, gender, paging = [30, 50], name = ('차은우','이지은'), gender = 'female')
        '''

    
    def column_list(self):
        with OracleConnection() as cursor:
            cursor.execute(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE table_name = :1 ",[self.table.upper()])

            rows = [col[0] for col in cursor.fetchall()]
            return rows

    @abstractmethod
    def sql(self):
        pass

    @classmethod
    def get_tables(cls):
        if cls._tables is None:
            cls._tables = cls.table_names()  # 처음 한 번만 실제로 DB에서 호출
        return cls._tables

    # 테이블 목록
    @staticmethod
    def table_names():
        with OracleConnection() as cursor:
            cursor.execute(f'SELECT DISTINCT TABLE_NAME FROM USER_TAB_COLUMNS')
            rows = [tbl[0] for tbl in cursor.fetchall()]
            return rows
