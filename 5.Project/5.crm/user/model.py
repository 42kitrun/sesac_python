import sys
sys.path.append('5.Project/5.crm')

from db.oracle import OracleDBPool
from db.tables import Tables
from db.crud import *

class User(Tables):
    def __init__(self, crud):
        super().__init__(crud)
        '''
        self.crud = crud
        self.table = '' # 하위 클래스에서 정하기
        '''
        self.table = 'users'
        
    def __call__(self):
        return self.crud.execute(self.table)

def user_list(query:dict):

    if 'listCount' not in query.keys():
        # 페이징처리 안함
        return User(DataGet(query))()
    
    # {'name': 'adsf', 'gender': 'Female', 'listCount': '20', 'page':'2'}
    # 페이징 처리한다
    removed_listCount = query.pop('listCount')
    removed_page = int(query.pop('page')) -1
    return User(DataGet(query, paging=[removed_listCount,removed_page]))()

if __name__ == '__main__':
    OracleDBPool.init_pool()
    print(User(DataGet(paging=[10,0]))())