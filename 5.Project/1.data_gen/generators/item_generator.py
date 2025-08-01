import sys

sys.path.append('5.Project/1.data_gen')
from generators.generator import GenerateData
from generators.id import IdGenerator
from generators.menu import MenuGenerator

class ItemGenerator:
    def __init__(self):
        self.__header = ['Id','Type','Name','UnitPrice']
        self.generator_map = {
            'Id': IdGenerator(),
            'Item':GenerateData(MenuGenerator('data/season_menu.txt'),10)()
        } # 기존 메뉴 55개 + 시즌 메뉴 10개 추가
        

    def generate(self, count:int=0)->tuple:
        items = []
        if count == 0 or count > 64: # 따로 count 안쓰면 다가져옴
            item_list = self.generator_map['Item']
            count = len(item_list)
        else:
            item_list = self.generator_map['Item'][:count]

        for i in range(count):
            id = GenerateData(self.generator_map['Id'])() # 대량 생산하지 않으므로 중복체크 안함
            _type, name, unit_price = item_list[i]
            items.append((id, _type, name, unit_price))
            
        return self.__header, items
        '''[(UUID('090d6ff8-2fc9-4b5b-86f5-bc0f810b8171'), 'Hand-Drip', '코스타리카 엘 세드로(Costa Rica C.O.E Winner El Cedro)', '12000')
          , (UUID('d1ba8153-b7fd-4cc3-93e8-b4b2f033d727'), 'Hand-Drip', '파나마 호세 게이샤(Panama Jose Geisha)', '10000')]
        '''
## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(GenerateData(ItemGenerator(),0)()[1])