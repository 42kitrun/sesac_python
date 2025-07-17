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


if __name__ == '__main__':
    OracleDBPool.init_pool()
    print(User(DataGet(paging=[10,0]))())