import sys
sys.path.append('5.Project/5.crm')

from db.oracle import OracleDBPool
from db.get import Get
from db.user import User,UserTop5Store


def user_list(query:dict):
    # 조회 쿼리 중에 컬럼명이 다른 컬럼의 키 변경
    if 'userId' in query:
        query['id'] = query.pop('userId')

    if 'listCount' not in query.keys():
        # 페이징처리 안함
        return Get(User(query))()
    
    # {'name': 'adsf', 'gender': 'Female', 'listCount': '20', 'page':'2'}
    # 페이징 처리한다
    removed_listCount = int(query.pop('listCount'))
    removed_page = int(query.pop('page'))
    return Get(User(query, paging=[removed_listCount,removed_page]))()
    # {'data': rows, 'paging':{'all_count':count,'list_cnt':self.list_cnt, 'this_page':self.page}}

def user_detail_top5(query:dict):
    # user_id만 전달됨
    if 'user_id' not in query:
        raise KeyError('user_detail_top5 should have only user_id key in query')
    
    return Get(UserTop5Store(query))
    # {'data': rows, 'paging':{'all_count':len(rows),'list_cnt':len(rows), 'this_page':1}}


if __name__ == '__main__':
    OracleDBPool.init_pool()
    print(Get(User(paging=[10,0]))())