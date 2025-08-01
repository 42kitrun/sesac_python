import sys
sys.path.append('5.Project/5.crm')

from db.oracle import OracleDBPool
from db.get import Get
from db.order import Order

def order_list(query:dict):
    # 조회 쿼리 중에 컬럼명이 다른 컬럼의 키 변경
    if 'userId' in query:
        query['user_id'] = query.pop('userId')

    if 'orderId' in query:
        query['ID'] = query.pop('orderId')

    if 'listCount' not in query.keys():
        # 페이징처리 안함
        return Get(Order(query))()
    
    # {'name': 'adsf', 'gender': 'Female', 'listCount': '20', 'page':'2'}
    # 페이징 처리한다
    removed_listCount = int(query.pop('listCount'))
    removed_page = int(query.pop('page'))
    return Get(Order(query, paging=[removed_listCount,removed_page]))()
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}


if __name__ == '__main__':
    OracleDBPool.init_pool()
    print(Get(Order(paging=[10,0]))())