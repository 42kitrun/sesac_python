import sys
sys.path.append('5.Project/5.crm')

from db.tables import Tables
from db.get import Get

class Order(Tables):

    def __init__(self, query:dict, **kwargs):
        '''
        self.tables = Tables.get_tables()  # 모든 객체가 같은 값 사용
        self.table = '' # 하위 클래스에서 정하기

        self.list_cnt = 0
        self.page = 1
        self.start_rownum = 0
        
        if kwargs: # 페이징 처리를 하겠다
            print('페이징 처리 입력값',kwargs)
            self.list_cnt = kwargs['paging'][0]
            self.page = kwargs['paging'][1]
            self.start_rownum = (self.page-1)*self.list_cnt

        self.query:dict = query
        print(f'{self.table} query', self.query)
        '''
        self.table = 'orders'
        super().__init__(query, **kwargs)
        

    def sql(self):
        
        sql = f"SELECT * FROM  CRM.{self.table} o" 
        
        #조회 조건이 있으면 활성화하세요
        if self.query:
            print(self.query)
            for k, v in self.query.items():
                ''' 테이블에 없는 컬럼 추가시 
                if k not in self.column_list(self.table):
                    if k == '': ## user_id
                        sql += 'JOIN CRM.USERS u ON u.ID = o.USER_ID '
                '''
                print(self.column_list())
                if k.upper() in self.column_list():
                    # print(f'{k} in CRM.{self.table}:{self.column_list()}')
                    if "WHERE 1=1" not in sql:
                        sql += ' WHERE 1=1 '
                    if k == 'name':
                        if '?' in v:
                            v = v.replace('?',"_")
                        if '*' in v:
                            v = v.repalce('*','%')
                        v = '%'+v+'%'
                        sql += f" AND {k.upper()} like '{v}'" # tuple이던 아니던 반복적으로 감싸도 중복없는 tuple
                    if k in ('user_id', 'order_type'):
                        sql += f" AND {k.upper()}  = '{v}' " # tuple이던 아니던 반복적으로 감싸도 중복없는 tuple
        
        count_sql = sql.replace('*','count(*)')

        if self.list_cnt:
            sql += f' ORDER BY id OFFSET {self.start_rownum} ROWS FETCH NEXT {self.list_cnt} ROWS ONLY'

        print('sql 조회문',sql)
        print('count_sql 조회문',count_sql)
        return sql, count_sql, self.list_cnt, self.page


class OrderSalesMonthly(Tables):
    def __init__(self,query):
        '''
        self.tables = Tables.get_tables()  # 모든 객체가 같은 값 사용
        self.table = '' # 하위 클래스에서 정하기
        '''
        super().__init__(query)    
        self.table = 'orders'
        self.store_id = query['store_id']

    def sql(self):
        print('OrderSalesMonthly')
        sql = '''SELECT SUBSTR(o.ORDER_DT,1,7) AS month
			     	  , sum(i.UNIT_PRICE ) AS revenue
                      , count(i.ID) AS count
                   FROM CRM.orders o
                   JOIN CRM.ORDERITEMS oi
                     ON oi.ORDER_ID = o.ID
                   JOIN CRM.ITEMS i 
                     ON i.ID = oi.ITEM_ID 
                  WHERE 1=1
                    AND o.STORE_ID = :sid
                  GROUP BY SUBSTR(o.ORDER_DT,1,7)
                  ORDER BY 1 DESC'''

        count_sql = f'SELECT COUNT(*) AS count FROM ({sql}) s'

        if self.list_cnt:
            sql += f' OFFSET {self.start_rownum} ROWS FETCH NEXT {self.list_cnt} ROWS ONLY'

        print('sql 조회문',sql)
        print('count_sql 조회문',count_sql)
        return  ((sql,{ "sid": self.store_id }), (count_sql,{ "sid": self.store_id }), self.list_cnt, self.page )