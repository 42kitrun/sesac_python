import random

class MenuGenerator:
    def __init__(self):
        self.__main_menu_file_path = '5.Project/1.data_gen/menu.txt' # 기존 판매 메뉴
        self.__new_desert = 10 ## 새로 개발한 디저트 가지수

    def generate_season_menu(self, count, idea_path = '5.Project/1.data_gen/season_menu.txt'):
        season_menu = []
        with open(idea_path) as file:
            flavor, kind = [line.strip().split(',') for line in file.readlines()]
            for _ in range(count):
                season_menu += [['SeasonDesert',f'{random.choice(flavor)} {random.choice(kind)}',random.randint(50,80)*100]]
            return season_menu

    def generate_menu(self,count, idea_path = '5.Project/1.data_gen/season_menu.txt'):
        menu = []
        with open(self.__main_menu_file_path, 'r', encoding='utf-8') as file:
            menu = [line.strip().split(',') for line in file.readlines()]
            menu+= self.generate_season_menu(count,idea_path)
            return menu

## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(MenuGenerator().generate_menu(10, idea_path = '5.Project/1.data_gen/season_menu.txt'))