import sys
sys.path.append('5.Project/5.crm')

from db.oracle import OracleDBPool
from db.get import Get
from db.item import Item
from db.monthly_sales import MonthlySales


def item_list(query:dict):
    if 'itemType' in query:
        query['ITEM_TYPE'] = query.pop('itemType')
    
    if 'itemId' in query:
        query['ID'] = query.pop('itemId')

    if 'listCount' not in query.keys():
        # 페이징처리 안함
        return Get(Item(query))()
    
    # {'name': 'adsf', 'gender': 'Female', 'listCount': '20', 'page':'2'}
    # 페이징 처리한다
    removed_listCount = int(query.pop('listCount'))
    removed_page = int(query.pop('page'))
    return Get(Item(query, paging=[removed_listCount,removed_page]))()
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}

def item_sales_monthly(query:dict):
    if 'itemId' in query:
        query['item_id'] = query.pop('itemId')

    if 'listCount' not in query.keys():
        # 페이징처리 안함
        return Get(MonthlySales(query))()
    
    # {'name': 'adsf', 'gender': 'Female', 'listCount': '20', 'page':'2'}
    # 페이징 처리한다
    removed_listCount = int(query.pop('listCount'))
    removed_page = int(query.pop('page'))
    return Get(MonthlySales(query, paging=[removed_listCount,removed_page]))()
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}
    

if __name__ == '__main__':
    OracleDBPool.init_pool()
    print(Get(Item(paging=[10,0]))())




