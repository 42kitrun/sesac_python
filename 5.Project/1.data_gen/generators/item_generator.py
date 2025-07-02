from generators.id_generator import IdGenerator
from generators.menu_generator import MenuGenerator

class ItemGenerator:
    def __init__(self):
        self.__uuid_history = set()

        self.id_gen = IdGenerator()
        self.item_gen = MenuGenerator('5.Project/1.data_gen/menu.txt').generate_menu()

    @property
    def uuid_history(self):
        return self.__uuid_history

    def generate_item(self, count:int=0)->list:
        items = []
        if count == 0:
            item_list = self.item_gen
            count = len(item_list)
        else:
            item_list = self.item_gen[:count]

        for i in range(count):
            id = self.id_gen.generate_id()  # uuid는 16바이트로 고정! if 문자열로 변환하면 일반적으로 32~36바이트(하이픈 포함)
            while id in self.__uuid_history:# 무작위 생성이므로 중복 발생할 가능성 염두
                id = self.id_gen.generate_id()
            self.__uuid_history.add(id)
            '''uuid 중복제거''' 
            _type, name, unit_price = item_list[i]

            items.append((id, _type, name, unit_price))
        return items
        '''[(UUID('090d6ff8-2fc9-4b5b-86f5-bc0f810b8171'), 'Hand-Drip', '코스타리카 엘 세드로(Costa Rica C.O.E Winner El Cedro)', '12000')
          , (UUID('d1ba8153-b7fd-4cc3-93e8-b4b2f033d727'), 'Hand-Drip', '파나마 호세 게이샤(Panama Jose Geisha)', '10000')]
        '''

# print(ItemGenerator().generate_item())        