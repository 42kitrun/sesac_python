import random

class MenuGenerator:
    def __init__(self, file_path):
        self.__file_path = file_path # 기존 판매 메뉴
        self.__new_desert = 10 ## 새로 개발한 디저트 가지수

    def generate_new_menu(self, count, idea_path = '5.Project/1.data_gen/new_menu.txt'):
        new_menu = []
        with open(idea_path) as file:
            flavor, kind = [line.strip().split(',') for line in file.readlines()]
            for _ in range(count):
                new_menu += [['New-Desert',f'{random.choice(flavor)} {random.choice(kind)}',random.randint(50,80)*100]]
            return new_menu

    def generate_menu(self):
        menu = []
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            menu = [line.strip().split(',') for line in file.readlines()]
            menu+= self.generate_new_menu(self.__new_desert, '5.Project/1.data_gen/new_menu.txt')
            return menu

# print(MenuGenerator('5.Project/1.data_gen/menu.txt').generate_item())