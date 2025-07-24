from db.oracle import *
from abc import ABC,abstractmethod

class Tables(ABC):
    _tables = None  # 클래스 변수로 선언
    
    # def __init_subclass__(cls):    # 클래스를 "정의"하는 시점(≠ 인스턴스 생성 시)에만 실행
    #     super().__init_subclass__()
    #     if isinstance():
    def __init__(self,  query:dict, **kwargs):
        self.tables = Tables.get_tables()  # 모든 객체가 같은 값 사용

        self.list_cnt = 0 # 기본값
        self.page = 1
        self.start_rownum = 0
        
        if kwargs: # 페이징 처리를 하겠다
            print('페이징 처리 입력값',kwargs)
            self.list_cnt = kwargs['paging'][0]
            self.page = kwargs['paging'][1]
            self.start_rownum = (self.page-1)*self.list_cnt

        # 오라클에서 :PARAM명 형식의 바인딩 시, 바인딩 파라미터 이름은 항상 대문자로 처리.
        self.query:dict = {k.upper():v for k,v in query.items()}
        print(f'{self.table} query', self.query)

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
    
    def common_sql(self):
        sql = f"SELECT * FROM  CRM.{self.table} t" 
        
        #조회 조건이 있으면 활성화하세요
        if self.query:
            print('self.query',self.query)
            for k, v in self.query.items():
                ''' 테이블에 없는 컬럼 추가시 
                if k not in self.column_list(self.table):
                    if k == '': ## user_id
                        sql += 'JOIN CRM.USERS u ON u.ID = t.USER_ID 
                '''
                print('self.column_list()',self.column_list())
                if k in self.column_list():
                    # print(f'{k} in CRM.{self.table}:{self.column_list()}')
                    if "WHERE 1=1" not in sql:
                        sql += ' WHERE 1=1 '
                    if k == 'NAME':
                        if '?' in v:
                            v = v.replace('?',"_")
                        if '*' in v:
                            v = v.repalce('*','%')
                        self.query[k] = f'%{v}%'.replace("%%","%")
                        sql += f" AND {k} like :{k}" # tuple이던 아니던 반복적으로 감싸도 중복없는 tuple
                    if k in ('GENDER', 'ID', 'STORE_TYPE', 'ITEM_TYPE','ORDER_TYPE','USER_ID'):
                        sql += f" AND {k} = :{k}" # tuple이던 아니던 반복적으로 감싸도 중복없는 tuple

        count_sql = sql.replace('*','count(*)')

        if self.list_cnt:
            sql += f' ORDER BY id OFFSET {self.start_rownum} ROWS FETCH NEXT {self.list_cnt} ROWS ONLY'

        sql = sql, self.query
        count_sql = count_sql, self.query

        print('sql 조회문',sql)
        print('count_sql 조회문',count_sql)
        return sql, count_sql, self.list_cnt, self.page


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
