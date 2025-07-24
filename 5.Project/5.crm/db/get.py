from db.oracle import *
from db.crud import Crud

class Get(Crud):
    
    def __init__(self, tables):
        '''
        self.tables = tables.sql()
        '''
        super().__init__(tables)
        self.list_cnt = 20
        self.page = 1
        
    
    def execute(self):
        
        sql, count_sql, self.list_cnt, self.page = self.tables

        rows = []
        count = ''
        with OracleConnection() as cursor:
            cursor.execute(sql[0], sql[1])
            rows = Get.dict_r(cursor)

        with OracleConnection() as cursor:
            cursor.execute(count_sql[0], count_sql[1])
            count = cursor.fetchone()[0]
            
        print('sql 조회 결과',rows[0])
        print('count_sql 조회 결과', count)
        return {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}