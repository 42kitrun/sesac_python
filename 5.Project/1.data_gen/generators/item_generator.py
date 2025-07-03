from generators.id_generator import IdGenerator
from generators.menu_generator import MenuGenerator

class ItemGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        self.item_gen = MenuGenerator('5.Project/1.data_gen/menu.txt').generate_menu()

    def generate_item(self, count:int=0)->list:
        items = []
        if count == 0:
            item_list = self.item_gen
            count = len(item_list)
        else:
            item_list = self.item_gen[:count]

        for i in range(count):
            id = self.id_gen.generate_id()  # uuid는 16바이트로 고정! if 문자열로 변환하면 일반적으로 32~36바이트(하이픈 포함)
            _type, name, unit_price = item_list[i]
            items.append((id, _type, name, unit_price))
        return items
        '''[(UUID('090d6ff8-2fc9-4b5b-86f5-bc0f810b8171'), 'Hand-Drip', '코스타리카 엘 세드로(Costa Rica C.O.E Winner El Cedro)', '12000')
          , (UUID('d1ba8153-b7fd-4cc3-93e8-b4b2f033d727'), 'Hand-Drip', '파나마 호세 게이샤(Panama Jose Geisha)', '10000')]
        '''
## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(ItemGenerator().generate_item())        