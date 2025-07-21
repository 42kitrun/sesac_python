import sys
sys.path.append('5.Project/5.crm')

from db.oracle import OracleDBPool
from db.tables import Tables
from db.crud import *

class Store(Tables):
    def __init__(self, crud):
        super().__init__(crud)
        '''
        self.crud = crud
        self.table = '' # 하위 클래스에서 정하기
        '''
        self.table = 'stores'
        
    def __call__(self):
        return self.crud.execute(self.table)

def store_list(query:dict):
    if 'storeType' in query:
        query['store_type'] = query.pop('storeType')

    print(query) 

    if 'listCount' not in query.keys():
        # 페이징처리 안함
        return Store(DataGet(query))()
    
    # {'name': 'adsf', 'type': '스타벅스', 'listCount': '20', 'page':'2'}
    # 페이징 처리한다
    removed_listCount = int(query.pop('listCount'))
    removed_page = int(query.pop('page'))
    return Store(DataGet(query, paging=[removed_listCount,removed_page]))()
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}

if __name__ == '__main__':
    OracleDBPool.init_pool()
    print(Store(DataGet(paging=[10,0]))())