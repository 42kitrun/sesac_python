from id_generator import IdGenerator
from datetime import datetime, date
import csv

class OrderGenerator:
    def __init__(self):
        self.__header = ['Id','OrderAt','StoreId','UserId']
        self.__uuid_history = set()

        self.id_gen = IdGenerator()
    
    @property
    def uuid_history(self):
        return self.__uuid_history
    
    def find_user_info(self, user_id):
        # bbc5ee4e-592d-4eed-85a1-79baf7c398e6,경예주,Female,34,1991-04-14,대구광역시 구로구 수밭서길 215
        with open(f'5.Project/1.data_gen/user.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == user_id:
                    return row
                
        print(f'유효하지 않은 store_id : {user_id}')
        return (user_id,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'','') # 유효하지 않은 store_id, 유효하지 않음을 확인한 시각


    def find_store_info(self, store_id):
        # 8569d76f-cfb2-472d-a235-525ac7d5a8ec,에이프릴커피 증미직영점,에이프릴커피,경상북도 울주군 마곡사로 124
        with open(f'5.Project/1.data_gen/store.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == store_id:
                    return row
        print(f'유효하지 않은 store_id : {store_id}')
        return (store_id,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'','') # 유효하지 않은 store_id, 유효하지 않음을 확인한 시각

    def generate_order(self\
                       , user_id='bbc5ee4e-592d-4eed-85a1-79baf7c398e6'\
                        ,store_id='8569d76f-cfb2-472d-a235-525ac7d5a8ec'):
        # 가장 먼저 유효한 거래인지 확인! 누가 어디에서 결재했는지
        user_info = self.find_user_info(user_id)
        store_info = self.find_store_info(store_id)

        id = self.id_gen.generate_id()  # uuid는 16바이트로 고정! if 문자열로 변환하면 일반적으로 32~36바이트(하이픈 포함)
        while id in self.__uuid_history:# 무작위 생성이므로 중복 발생할 가능성 염두
            id = self.id_gen.generate_id()
        self.__uuid_history.add(id)

        return (id, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), store_info[0], user_info[0])
        '''[(UUID('134a067b-6409-4fc1-a557-327f6387be4c'), '2025-07-02 17:22:55', '8569d76f-cfb2-472d-a235-525ac7d5a8ec', 'bbc5ee4e-592d-4eed-85a1-79baf7c398e6')]
        '''

    def save_order(self):
        order = self.generate_order()
        with open(f'5.Project/1.data_gen/order.csv', 'r+') as csvfile:# a+ 읽기 쓰기 가능
            csv_writer = csv.writer(csvfile)
            
            if not csvfile.read(2):
                csv_writer.writerow(self.__header)

            csv_writer.writerow(order)

        print('주문정보를 저장했습니다')
        return order

print(OrderGenerator().save_order())        