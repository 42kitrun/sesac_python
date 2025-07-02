from id_generator import IdGenerator
from datetime import datetime, date
import csv

class OrderItemGenerator:
    def __init__(self):
        self.__header = ['Id','OrderId','ItemId']
        self.__uuid_history = set()

        self.id_gen = IdGenerator()
    
    @property
    def uuid_history(self):
        return self.__uuid_history
    
    def find_order_info(self, order_id):
        # Id,OrderAt,StoreId,UserId
        # f8d2e618-ab11-439f-a321-b0593f7f70ec,2025-07-02 23:25:05,8569d76f-cfb2-472d-a235-525ac7d5a8ec,bbc5ee4e-592d-4eed-85a1-79baf7c398e6
        with open(f'5.Project/1.data_gen/order.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == order_id:
                    return row

        print(f'유효하지 않은 order_id : {order_id}')
        return order_id,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'','' # 유효하지 않은 order_id, 유효하지 않음을 확인한 시각

    def find_item_info(self, item_id):
        # Id,Name,Type,UnitPrice
        # ceb93608-e31c-4a16-826f-c516eff557a5,Hand-Drip,코스타리카 엘 세드로(Costa Rica C.O.E Winner El Cedro),12000
        with open(f'5.Project/1.data_gen/item.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == item_id:
                    return row

        print(f'유효하지 않은 item_id : {item_id}')
        return item_id,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'',0 # 유효하지 않은 item_id, 유효하지 않음을 확인한 시각


    def generate_order_items( self\
                            , order_id='f8d2e618-ab11-439f-a321-b0593f7f70ec'
                            , item_list=['ceb93608-e31c-4a16-826f-c516eff557a5' # Hand-Drip,코스타리카 엘 세드로
                                        ,'1e30afde-8841-49c3-9a31-f82575da956b' # House Beverage,하우스 주스 제주 감귤로 착즙한
                                        ,'a7e7b713-f7d0-410e-9017-ff5a2101a71f' # Desert,프레시 레몬 케이크
                                        ,'c0868b45-43b1-4d28-b74d-6a9518428ae5' # New-Desert,한라봉 푸딩
                                        ])->list:
        # 가장 먼저 유효한 거래인지 확인! 어떤 아이템들이 주문에서 결재되었는지
        order_info = self.find_order_info(order_id)
        items_info = [self.find_item_info(item) for item in item_list]

        order_items = []
        for n in range(len(items_info)):
            id = self.id_gen.generate_id()  # uuid는 16바이트로 고정! if 문자열로 변환하면 일반적으로 32~36바이트(하이픈 포함)
            while id in self.__uuid_history:# 무작위 생성이므로 중복 발생할 가능성 염두
                id = self.id_gen.generate_id()
            self.__uuid_history.add(id)

            order_items.append((id, order_info[0], items_info[n][0]))
        return order_items
        '''[(UUID('65e08b44-7a6c-45df-abf4-74334537b50e'), 'f8d2e618-ab11-439f-a321-b0593f7f70ec', 'ceb93608-e31c-4a16-826f-c516eff557a5')
          , (UUID('cc66dad7-be24-449c-87b9-5b30bc0d1e8b'), 'f8d2e618-ab11-439f-a321-b0593f7f70ec', '1e30afde-8841-49c3-9a31-f82575da956b')
          , (UUID('d6b23d1f-3f10-4dbd-8ea2-a372792c0bcc'), 'f8d2e618-ab11-439f-a321-b0593f7f70ec', 'a7e7b713-f7d0-410e-9017-ff5a2101a71f')
          , (UUID('a5af33fc-a191-4489-b14f-8bc59f878d0c'), 'f8d2e618-ab11-439f-a321-b0593f7f70ec', 'c0868b45-43b1-4d28-b74d-6a9518428ae5')]
        '''

    def save_order_items(self,order_id='f8d2e618-ab11-439f-a321-b0593f7f70ec'
                            , item_list=['ceb93608-e31c-4a16-826f-c516eff557a5' # Hand-Drip,코스타리카 엘 세드로
                                        ,'1e30afde-8841-49c3-9a31-f82575da956b' # House Beverage,하우스 주스 제주 감귤로 착즙한
                                        ,'a7e7b713-f7d0-410e-9017-ff5a2101a71f' # Desert,프레시 레몬 케이크
                                        ,'c0868b45-43b1-4d28-b74d-6a9518428ae5' # New-Desert,한라봉 푸딩
                                        ]):
        order_items = self.generate_order_items(order_id,item_list)
        with open(f'5.Project/1.data_gen/orderitem.csv', 'r+') as csvfile:# a+ 읽기 쓰기 가능
            csv_writer = csv.writer(csvfile)
            
            if not csvfile.read(2):
                csv_writer.writerow(self.__header)

            csv_writer.writerows(order_items)

        print('주문정보를 저장했습니다')
        return order_items

print(OrderItemGenerator().save_order_items())        