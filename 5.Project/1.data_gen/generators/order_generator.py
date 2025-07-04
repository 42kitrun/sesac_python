from id_generator import IdGenerator
from id_handler import select_id

from random import randint

class OrderGenerator:
    def __init__(self):
        self.__header = ['Id','OrderAt','StoreId','UserId']
        self.id_gen = IdGenerator()
    
    def generate_order(self,count):
        data = []

        for _ in range(count):
            # order_id 생성
            id = self.id_gen.generate_id()  # 주문 1번당 id 1개 생성 여러 주문을 한번에 생성하지 않음
            user_id = select_id('user')
            store_id = select_id('store')

            data.append((id,f'{randint(2000,2025)}-{randint(1,12):02d}-{randint(1,28):02d} {randint(7,21):02d}:{randint(0,59):02d}:{randint(0,59):02d}' , store_id, user_id))

        return self.__header, data
        '''[(UUID('134a067b-6409-4fc1-a557-327f6387be4c'), '2025-07-02 17:22:55', '8569d76f-cfb2-472d-a235-525ac7d5a8ec', 'bbc5ee4e-592d-4eed-85a1-79baf7c398e6')]
        '''

## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(OrderGenerator().generate_order(10_000))          