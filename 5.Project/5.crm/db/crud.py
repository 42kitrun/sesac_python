from db.oracle import *

# cursor 결과를 dict로 변환
def dict_r(cursor):
    columns = [col[0].lower() for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

# 테이블 목록
def table_names():
    with OracleConnection() as cursor:
        cursor.execute(f'SELECT DISTINCT TABLE_NAME FROM USER_TAB_COLUMNS')
        rows = [tbl[0] for tbl in cursor.fetchall()]
        return rows

def column_list(table):
    with OracleConnection() as cursor:
        cursor.execute(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE table_name = :1 ",[table.upper()])
        
        rows = [col[0] for col in cursor.fetchall()]
        return rows

# ------------------------------------------------------------------------------------

class Crud(ABC):
    _tables = None  # 클래스 변수로 선언

    @classmethod
    def get_tables(cls):
        if cls._tables is None:
            cls._tables = table_names()  # 처음 한 번만 실제로 DB에서 호출
        return cls._tables

    def __init__(self):
        self.tables = self.get_tables()  # 모든 객체가 같은 값 사용

    @abstractmethod
    def execute(self, target):
        pass

class DataGet(Crud):
    def __init__(self, *attrs, **kwargs):
        self.list_cnt = 0
        self.start_rownum = 0

        if attrs == ():
            attrs = ('paging',)

        if set(attrs) != set(kwargs):
            raise ValueError(self.__repr__())
        
        if 'paging' in attrs:
            self.list_cnt = kwargs['paging'][0]
            self.start_rownum = kwargs['paging'][1]
            attrs = [attr for attr in attrs if attr != 'paging']

        self.col_names:tuple = tuple(attrs)
        self.criteria:dict = kwargs

    
    def __repr__(self):
        return '''
            DataGet( *attr=('paging',), **kwargs)
            DataGet(paging=[list_cnt, start_rownum])
            예) DataGet(paging=[20, 80]) (0 이 시작) 80번째 데이터부터 20개
            예) DataGet(name, gender, name = ('차은우','이지은'), gender = 'female')
            예) DataGet(paging, name, gender, paging = [30, 50], name = ('차은우','이지은'), gender = 'female')
        '''

    def sql(self,table):
        columns = column_list(table)
        print(columns)
        
        sql = f"SELECT * FROM  CRM.{table} WHERE 1=1" 
        
        for attr in self.col_names:
            if attr.upper() not in columns:
                raise ValueError("존재하지 않는 컬럼(속성)입니다.")
            sql += f" AND {attr} in {tuple(self.kwargs[attr])}" # tuple이던 아니던 반복적으로 감싸도 중복없는 tuple
        
        if self.start_rownum or self.list_cnt:
            sql += " ORDER BY id"
        if self.start_rownum:
            sql += f' OFFSET {self.start_rownum} ROWS'
        if self.list_cnt:
            sql += f' FETCH NEXT {self.list_cnt} ROWS ONLY'

        return sql
    
    def execute(self, target):
        if target.upper() not in Crud.tables:
            raise ValueError("존재하지 않는 테이블입니다.")

        sql = self.sql(target)

        with OracleConnection() as cursor:
            cursor.execute(sql)
            rows = dict_r(cursor)
            return rows


# ------------------------------------------------------------------------------------





# ------------------------------------------------------------------------------------