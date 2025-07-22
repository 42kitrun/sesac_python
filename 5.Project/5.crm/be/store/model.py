import sys
sys.path.append('5.Project/5.crm')

from db.oracle import OracleDBPool
from db.tables import Tables
from db.get import Get

class Store(Tables):

    def __init__(self, query:dict, **kwargs):
        '''
        self.tables = Tables.get_tables()  # 모든 객체가 같은 값 사용
        self.table = '' # 하위 클래스에서 정하기
        '''
        super().__init__()
        self.table = 'stores'
        self.list_cnt = 0
        self.page = 1
        self.start_rownum = 0
        
        if kwargs: # 페이징 처리를 하겠다
            print('페이징 처리 입력값',kwargs)
            self.list_cnt = kwargs['paging'][0]
            self.page = kwargs['paging'][1]
            self.start_rownum = (self.page-1)*self.list_cnt

        self.query:dict = query

    def sql(self):
        # columns = self.column_list(table) 추후 검증 로직
        
        sql = f"SELECT * FROM  CRM.{self.table} WHERE 1=1" 
        
        if self.query:
            for k, v in self.query.items():
                if k == 'name':
                    if '?' in v:
                        v = v.replace('?',"_")
                    if '*' in v:
                        v = v.repalce('*','%')
                    v = '%'+v+'%'
                    sql += f" AND {k.upper()} like '{v}'" # tuple이던 아니던 반복적으로 감싸도 중복없는 tuple
                if k in ('id', 'store_type'):
                    sql += f" AND {k.upper()}  = '{v}' " # tuple이던 아니던 반복적으로 감싸도 중복없는 tuple
        
        count_sql = sql.replace('*','count(*)')

        if self.list_cnt:
            sql += f' ORDER BY id OFFSET {self.start_rownum} ROWS FETCH NEXT {self.list_cnt} ROWS ONLY'

        print('sql 조회문',sql)
        print('count_sql 조회문',count_sql)
        return sql, count_sql, self.list_cnt, self.page

# ------------------------------------------------------------------------------------------------------

def store_list(query:dict):
    if 'storeType' in query:
        query['store_type'] = query.pop('storeType')

    if 'listCount' not in query.keys():
        # 페이징처리 안함
        return Get(Store(query))()
    
    # {'name': 'adsf', 'gender': 'Female', 'listCount': '20', 'page':'2'}
    # 페이징 처리한다
    removed_listCount = int(query.pop('listCount'))
    removed_page = int(query.pop('page'))
    return Get(Store(query, paging=[removed_listCount,removed_page]))()
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}

if __name__ == '__main__':
    OracleDBPool.init_pool()
    print(Get(Store(paging=[10,0]))())