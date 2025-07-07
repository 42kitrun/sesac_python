import sys
sys.path.append('5.Project/1.data_gen')
from generators.generator import GenerateData
from generators.id import IdGenerator
# from generators.id_handler import select_id
import csv
from random import sample, choice, choices, randint
import numpy as np

class OrderItemGenerator:
    def __init__(self):
        self.__header = ['Id','OrderId','ItemId']
        self.id_map = {'order':[], 'item':[]}
        self.generator_map = {
            'Id': IdGenerator()
        }

    def load_id(self, _type, count:int):
        with open(f'5.Project/1.data_gen/output/{_type}.csv', 'r',encoding='utf-8') as csvfile:
            # 파일 내용 불러오기
            # DictReader로 컬럼 순서가 바뀌어도 값을 가져오는데 문제 없음, fieldnames로 일부 컬럼만 가져올 수 있음
            csv_list = list(map(lambda x : x['Id'], csv.DictReader(csvfile,fieldnames=['Id'])))
            return {'order':lambda:sample(csv_list, k=count) # 처방은 전체 OrderId 중에서 count 만큼만(모두 1개씩 사는 최소 경우)
                   ,'item':lambda:csv_list[1:]}[_type]() # item은 전체 메뉴판(header 제거)에서 복원 추출

    def generate( self, count):
        order_items = []
        order_num = 0

        for k in self.id_map.keys():
            _type = k.lower().replace('id','')
            self.id_map[k] = self.load_id(_type,count)

        print(self.id_map)

        while len(order_items) <= count:
            items_id_list = choices(self.id_map['item'], k=randint(1,8)) # 1 ~ 8개 복원추출
            order_num += len(items_id_list)
            order_grp = list(zip(
                                 [GenerateData(self.generator_map['Id'])() for _ in range(len(items_id_list))] # orderitem_id
                                ,[choice(self.id_map['item'])]* len(items_id_list) # order_id
                                ,items_id_list # item_it
                        ))

            order_items.extend(order_grp)

        return self.__header, order_items[:count]
        '''[(UUID('65e08b44-7a6c-45df-abf4-74334537b50e'), 'f8d2e618-ab11-439f-a321-b0593f7f70ec', 'ceb93608-e31c-4a16-826f-c516eff557a5')
          , (UUID('cc66dad7-be24-449c-87b9-5b30bc0d1e8b'), 'f8d2e618-ab11-439f-a321-b0593f7f70ec', '1e30afde-8841-49c3-9a31-f82575da956b')
          , (UUID('d6b23d1f-3f10-4dbd-8ea2-a372792c0bcc'), 'f8d2e618-ab11-439f-a321-b0593f7f70ec', 'a7e7b713-f7d0-410e-9017-ff5a2101a71f')
          , (UUID('a5af33fc-a191-4489-b14f-8bc59f878d0c'), 'f8d2e618-ab11-439f-a321-b0593f7f70ec', 'c0868b45-43b1-4d28-b74d-6a9518428ae5')]
        '''
## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(GenerateData(OrderItemGenerator(),2)())