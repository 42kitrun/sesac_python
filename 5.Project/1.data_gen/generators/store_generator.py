from generators.generator import GenerateData
from generators.id import IdGenerator
from generators.store_name import StoreNameGenerator
from generators.address import AddressGenerator

class StoreGenerator:
    def __init__(self):
        self.__header = ['Id','Name','Type','Address']
        # 초기 객체를 불러올때는 처음 한번에 큰 데이터 가져오기
        self.generator_map = {
            'Id': IdGenerator(),
            'Name': StoreNameGenerator('5.Project/1.data_gen/data/store_names.txt'),
            'Type':'',
            'Address':AddressGenerator('5.Project/1.data_gen/data/address_data.txt')
        }
        '''
        self.id_gen = IdGenerator()
        self.store_name_gen = StoreNameGenerator('5.Project/1.data_gen/data/store_names.txt')
        self.address_gen = AddressGenerator('5.Project/1.data_gen/data/address_data.txt')
        '''

    def generate(self, count:int)->tuple:
        stores = []
        for _ in range(count):
            id = GenerateData(self.generator_map['Id'])()
            brand, store_name = GenerateData(self.generator_map['Name'])()
            name = f'{brand} {store_name}'
            address = GenerateData(self.generator_map['Address'])()
            stores.append((id, name, brand, address))

        return self.__header, stores
        '''[(UUID('02e54da6-c36c-4242-ac90-0868ef5df9b1'), '팀홀튼 동여의도3호점', '팀홀튼', '전북특별자치도 기장군 여원로 158')
          , (UUID('9803e939-66a7-45d9-ab02-b7af3d3d0951'), '카페드롭탑 판교3호점', '카페드롭탑', '경상북도 완주군 현풍동로20길 96')]
        '''
## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    # print(GenerateData(StoreGenerator(),4)()[0]) # 헤더
    print(str(GenerateData(StoreGenerator(),4)()[1])) # 데이터셋