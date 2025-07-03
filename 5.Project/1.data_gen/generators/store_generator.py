from output import DisplayData
from id_generator import IdGenerator
from store_name_generator import StoreNameGenerator
from address_generator import AddressGenerator

class StoreGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        self.store_name_gen = StoreNameGenerator('5.Project/1.data_gen/store_names.txt')
        self.address_gen = AddressGenerator('5.Project/1.data_gen/address_data.txt')

    def generate_store(self, count:int)->list:
        stores = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            brand, store_name = self.store_name_gen.generate_store_name()
            name = f'{brand} {store_name}'
            address = self.address_gen.generate_address()
            stores.append((id, name, brand, address))

        DisplayData().save_csv('store',stores)
        return stores
        '''[(UUID('02e54da6-c36c-4242-ac90-0868ef5df9b1'), '팀홀튼 동여의도3호점', '팀홀튼', '전북특별자치도 기장군 여원로 158')
          , (UUID('9803e939-66a7-45d9-ab02-b7af3d3d0951'), '카페드롭탑 판교3호점', '카페드롭탑', '경상북도 완주군 현풍동로20길 96')]
        '''
## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(StoreGenerator().generate_store(4))        