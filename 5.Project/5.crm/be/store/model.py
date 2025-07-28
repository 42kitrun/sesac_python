import sys
sys.path.append('5.Project/5.crm')

from db.oracle import OracleDBPool
from db.get import Get
from db.store import Store, StoreLoyalty
from db.monthly_sales import MonthlySales

def store_list(query:dict):
    if 'storeType' in query:
        query['store_type'] = query.pop('storeType')
    
    if 'storeId' in query:
        query['ID'] = query.pop('storeId')

    if 'listCount' not in query.keys():
        # 페이징처리 안함
        return Get(Store(query))()
    
    # {'name': 'adsf', 'gender': 'Female', 'listCount': '20', 'page':'2'}
    # 페이징 처리한다
    removed_listCount = int(query.pop('listCount'))
    removed_page = int(query.pop('page'))
    return Get(Store(query, paging=[removed_listCount,removed_page]))()
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}

def store_sales_monthly(query:dict):
    # 조회 쿼리 중에 컬럼명이 다른 컬럼의 키 변경
    if 'storeId' in query:
        print(query.keys())
        query['STORE_ID'] = query.pop('storeId')

    if 'listCount' not in query.keys():
        # 페이징처리 안함
        return Get(MonthlySales(query))()

    # {'name': 'adsf', 'gender': 'Female', 'listCount': '20', 'page':'2'}
    # 페이징 처리한다
    removed_listCount = int(query.pop('listCount',None)) # 키 없으면 무시
    removed_page = int(query.pop('page',None)) # 키 없으면 무시
    return Get(MonthlySales(query, paging=[removed_listCount,removed_page]))()
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}


def store_loyalty(query:dict):
    # 조회 쿼리 중에 컬럼명이 다른 컬럼의 키 변경
    if 'storeId' in query:
        print(query.keys())
        query['store_id'] = query.pop('storeId')

    if 'listCount' not in query.keys():
        # 페이징처리 안함
        return Get(StoreLoyalty(query))()

    # {'name': 'adsf', 'gender': 'Female', 'listCount': '20', 'page':'2'}
    # 페이징 처리한다
    removed_listCount = int(query.pop('listCount'))
    removed_page = int(query.pop('page'))
    return Get(StoreLoyalty(query, paging=[removed_listCount,removed_page]))()
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}


if __name__ == '__main__':
    OracleDBPool.init_pool()
    print(Get(Store(paging=[10,0]))())