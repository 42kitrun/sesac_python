import sys
sys.path.append('5.Project/5.crm')

from db.oracle import OracleDBPool
from db.get import Get
from db.store import Store

def store_list(query:dict):
    if 'storeType' in query:
        query['store_type'] = query.pop('storeType')
    
    if 'storeId' in query:
        query['id'] = query.pop('storeId')

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