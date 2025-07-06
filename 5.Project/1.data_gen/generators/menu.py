from generators.generator import GenerateData
import random

class MenuGenerator:
    def __init__(self, season_menu_file_path):
        self.season_menu_file_path = season_menu_file_path
        self.__main_menu_file_path = '5.Project/1.data_gen/data/menu.txt' # 기존 판매 메뉴
        self.__new_desert = 10 ## 새로 개발한 디저트 가지수

    def generate_season_menu(self, count):
        season_menu = []
        with open(self.season_menu_file_path) as file:
            flavor, kind = [line.strip().split(',') for line in file.readlines()]
            for _ in range(count):
                season_menu += [('SeasonDesert',f'{random.choice(flavor)} {random.choice(kind)}',random.randint(30,50)*100)]
            return season_menu

    # 전체 메뉴 생성
    def generate(self,count):
        '''기존 메뉴 + 시즌 메뉴 count개 추가, 시즌 메뉴 파일의 path와 함께 입력'''
        self.__new_desert = count
        menu = []
        # 기존 메뉴(main_menu)는 테라로사 메뉴 활용
        with open(self.__main_menu_file_path, 'r', encoding='utf-8') as file:
            menu = [ tuple(line.strip().split(',')) for line in file.readlines()]
            menu+= self.generate_season_menu(self.__new_desert)
            return menu

## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(GenerateData(MenuGenerator('5.Project/1.data_gen/data/season_menu.txt'),10)())