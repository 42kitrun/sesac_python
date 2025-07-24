import sys
sys.path.append('5.Project/5.crm')

from db.tables import Tables

class Order(Tables):

    def __init__(self, query:dict, **kwargs):
        '''
        self.tables = Tables.get_tables()  # 모든 객체가 같은 값 사용
        self.table = '' # 하위 클래스에서 정하기

        self.list_cnt = 0 # 기본값
        self.page = 1
        self.start_rownum = 0
        
        if kwargs: # 페이징 처리를 하겠다
            print('페이징 처리 입력값',kwargs)
            self.list_cnt = kwargs['paging'][0]
            self.page = kwargs['paging'][1]
            self.start_rownum = (self.page-1)*self.list_cnt

         # 오라클에서 :PARAM명 형식의 바인딩 시, 바인딩 파라미터 이름은 항상 대문자로 처리.
        self.query:dict = {k.upper():v for k,v in query.items()}
        print(f'{self.table} query', self.query)
        '''
        self.table = 'orders'
        super().__init__(query, **kwargs)
        

    def sql(self):
        return super().common_sql()