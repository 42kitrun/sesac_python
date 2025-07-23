from db.oracle import *
from db.crud import Crud

class Get(Crud):
    
    def __init__(self, tables):
        '''
        self.tables = tables.sql()
        '''
        super().__init__(tables)
        self.list_cnt = 0
        self.page = 1
        
    
    def execute(self):
        print('type(self.tables[1])',type(self.tables[1]))
        if len(self.tables) == 2 and type(self.tables[1]) == dict:
            sql, params = self.tables

            with OracleConnection() as cursor:
                cursor.execute(sql, params)
                rows = Get.dict_r(cursor)
                return {'data': rows, 'paging':{'all_count':len(rows),'list_cnt':len(rows), 'this_page':1}}
        
        elif len(self.tables)==4:
            len(self.tables) == 2 and type(self.tables[1]) == dict
            
        else:
            sql, count_sql, self.list_cnt, self.page = self.tables

            rows = []
            count = ''
            with OracleConnection() as cursor:
                cursor.execute(sql)
                rows = Get.dict_r(cursor)

            with OracleConnection() as cursor:
                cursor.execute(count_sql)
                count = cursor.fetchone()[0]

            print('sql 조회 결과',rows[0])
            print('count_sql 조회 결과', count)
            return {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}