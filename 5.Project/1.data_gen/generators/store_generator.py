from generators.id_generator import IdGenerator
from generators.store_name_generator import StoreNameGenerator
from generators.address_generator import AddressGenerator

class StoreGenerator:
    def __init__(self):
        self.__uuid_history = set()

        self.id_gen = IdGenerator()
        self.store_name_gen = StoreNameGenerator('5.Project/1.data_gen/store_names.txt')
        self.address_gen = AddressGenerator('5.Project/1.data_gen/address_data.txt')
    
    @property
    def uuid_history(self):
        return self.__uuid_history

    def generate_store(self, count:int)->list:
        stores = []
        for _ in range(count):
            id = self.id_gen.generate_id()  # uuid는 16바이트로 고정! if 문자열로 변환하면 일반적으로 32~36바이트(하이픈 포함)
            while id in self.__uuid_history:# 무작위 생성이므로 중복 발생할 가능성 염두
                id = self.id_gen.generate_id()
            self.__uuid_history.add(id)
            '''uuid 중복제거''' 
            brand, store_name = self.store_name_gen.generate_store_name()
            name = f'{brand} {store_name}'
            address = self.address_gen.generate_address()
            stores.append((id, name, brand, address))
        return stores
        '''[(UUID('02e54da6-c36c-4242-ac90-0868ef5df9b1'), '팀홀튼 동여의도3호점', '팀홀튼', '전북특별자치도 기장군 여원로 158')
          , (UUID('9803e939-66a7-45d9-ab02-b7af3d3d0951'), '카페드롭탑 판교3호점', '카페드롭탑', '경상북도 완주군 현풍동로20길 96')]
        '''

# print(StoreGenerator().generate_user(2))        