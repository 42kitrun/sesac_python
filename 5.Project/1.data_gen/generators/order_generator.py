import sys
sys.path.append('5.Project/1.data_gen')
from generators.generator import GenerateData
from generators.id import IdGenerator
from csv import DictReader
from random import randint, choices, choice

class OrderGenerator:
    def __init__(self):
        self.__header = ['Id','OrderAt','StoreId','UserId']
        self.id_map = {'user':[], 'store':[]}
        self.generator_map = {
            'Id': IdGenerator()
        }
    
    def load_id(self, _type, count:int):
        with open(f'5.Project/1.data_gen/output/{_type}.csv', 'r',encoding='utf-8') as csvfile:
            # 파일 내용 불러오기
            # DictReader로 컬럼 순서가 바뀌어도 값을 가져오는데 문제 없음, fieldnames로 일부 컬럼만 가져올 수 있음
            csv_list = list(map(lambda x : x['Id'], DictReader(csvfile,fieldnames=['Id'])))
            if len(csv_list) > count :
                return choices(csv_list[1:], k=count) # 전체 id 중에서 복원 추출로 count 만큼 추출
            else:
                return csv_list[1:] # 생성하려는 수가 storeid나 userid 보다 크면 헤더를 제외한 모든 데이터셋

    def generate(self,count) -> tuple:
        data = []

        self.id_map['user'] = self.load_id('user',count)
        self.id_map['store'] = self.load_id('store',count)

        for _ in range(count):
            # order_id 생성
            id = GenerateData(self.generator_map['Id'])()  # 주문 1번당 id 1개 생성 여러 주문을 한번에 생성하지 않음
            user_id = choice(self.id_map['user'])
            store_id = choice(self.id_map['store'])

            data.append((id,f'{randint(2000,2025)}-{randint(1,12):02d}-{randint(1,28):02d} {randint(7,21):02d}:{randint(0,59):02d}:{randint(0,59):02d}' , store_id, user_id))

        return self.__header, data
        '''[(UUID('134a067b-6409-4fc1-a557-327f6387be4c'), '2025-07-02 17:22:55', '8569d76f-cfb2-472d-a235-525ac7d5a8ec', 'bbc5ee4e-592d-4eed-85a1-79baf7c398e6')]
        '''

## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(GenerateData(OrderGenerator(),2)())          