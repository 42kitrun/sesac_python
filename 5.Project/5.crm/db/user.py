import sys
sys.path.append('5.Project/5.crm')

from db.oracle import OracleConnection
from db.tables import Tables

class User(Tables):

    def __init__(self, query:dict, **kwargs):
        '''
        self.tables = Tables.get_tables()  # 모든 객체가 같은 값 사용
        self.table = '' # 하위 클래스에서 정하기

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
        '''
        self.table = 'users'
        super().__init__(query, **kwargs)

    def column_list(self):
        with OracleConnection() as cursor:
            cursor.execute(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE table_name = :1 ",[self.table.upper()])

            rows = [col[0] for col in cursor.fetchall()]
            return rows

    def sql(self):
        # columns = self.column_list(table) 추후 검증 로직

        return super().common_sql()

class UserTop5Store(Tables):
    def __init__(self,query, **kwargs):
        '''
        self.tables = Tables.get_tables()  # 모든 객체가 같은 값 사용
        self.table = '' # 하위 클래스에서 정하기

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
        '''
        self.table = 'orders'
        super().__init__(query, **kwargs)    

    def sql(self):
        print('UserTop5Store')
        sql =   '''SELECT store_name
                        , order_count
                     FROM (SELECT store_id
                     			, max(name) AS store_name
                                , COUNT(*) AS order_count
                                , RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
                             FROM CRM.orders o 
                             JOIN CRM.stores s
                               ON s.id = o.store_id
                            WHERE user_id = :USER_ID
                            GROUP BY store_id
                          ) ranked
                    WHERE rnk <= 5
                    ORDER BY order_count DESC''',  self.query

        count_sql = f'SELECT COUNT(*) AS count FROM ({sql[0]}) s', self.query
        
        if self.list_cnt:
            sql += f' ORDER BY id OFFSET {self.start_rownum} ROWS FETCH NEXT {self.list_cnt} ROWS ONLY'

        print('sql 조회문',sql)
        print('count_sql 조회문',count_sql)
        return sql, count_sql, self.list_cnt, self.page