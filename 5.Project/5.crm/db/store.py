import sys
sys.path.append('5.Project/5.crm')

from db.tables import Tables

class Store(Tables):

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
        self.table = 'stores'
        super().__init__(query, **kwargs)

    def sql(self):
        # columns = self.column_list(table) 추후 검증 로직
        
        return super().common_sql()

class StoreSalesMonthly(Tables):
    def __init__(self,query:dict, **kwargs):
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
        print('StoreSalesMonthly')
        sql = '''SELECT SUBSTR(o.ORDER_DT,1,7) AS month
			     	  , sum(i.UNIT_PRICE ) AS revenue
                      , count(i.ID) AS count
                   FROM CRM.orders o
                   JOIN CRM.ORDERITEMS oi
                     ON oi.ORDER_ID = o.ID
                   JOIN CRM.ITEMS i 
                     ON i.ID = oi.ITEM_ID 
                  WHERE 1=1
                    AND o.STORE_ID = :STORE_ID
                  GROUP BY SUBSTR(o.ORDER_DT,1,7)
                  ORDER BY 1 DESC'''

        count_sql = f'SELECT COUNT(*) AS count FROM ({sql}) s'

        if self.list_cnt:
            sql += f' OFFSET {self.start_rownum} ROWS FETCH NEXT {self.list_cnt} ROWS ONLY'

        print('sql 조회문',sql)
        print('count_sql 조회문',count_sql)
        return (sql,self.query), (count_sql,self.query), self.list_cnt, self.page 

class StoreLoyalty(Tables):
    def __init__(self,query:dict, **kwargs):
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
        print('StoreLoyalty')
        sql = '''SELECT USER_ID
                      , NAME
                      , FREQUENCY
                   FROM (SELECT o.USER_ID
                              , max(u.NAME) AS NAME
                              , count(1) AS FREQUENCY
                              , RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
                     	   FROM CRM.ORDERS o
                     	   JOIN CRM.USERS u 
                    	     ON u.ID = o.USER_ID
                    	  WHERE 1=1
                    	    AND o.STORE_ID = :STORE_ID
                    	  GROUP BY o.USER_ID
                        ) ranked
                  WHERE rnk <= 5
                  ORDER BY FREQUENCY DESC'''

        count_sql = f'SELECT COUNT(*) AS count FROM ({sql}) s'

        if self.list_cnt:
            sql += f' OFFSET {self.start_rownum} ROWS FETCH NEXT {self.list_cnt} ROWS ONLY'

        print('sql 조회문',sql)
        print('count_sql 조회문',count_sql)
        return (sql,self.query), (count_sql,self.query), self.list_cnt, self.page 