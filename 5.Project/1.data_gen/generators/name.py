import random

class NameGenerator:
    # def __init__(self):
        # self.names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
        # 기존 하드코딩 되어 있던걸, 파일을 통해서 읽는 방식으로 변경해보기
    def __init__(self, file_path):
        self.__file_path = file_path

    def generate(self)->dict:
        dic_name = dict()
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                s_line = line.strip().split(',')
                dic_name[s_line[0]]=  random.choice(s_line[1:])
        return dic_name
    '''{'sung': '양', 'f_1960': '혜란', 'm_1960': '영정', 'f_1970': '정난', 'm_1970': '정석'
    , 'f_1980': '영진', 'm_1980': '성국', 'f_1990': '은솔', 'm_1990': '준혁', 'f_2000': '가은'
    , 'm_2000': '형준', 'f_2010': '지아', 'm_2010': '시완', 'f_2020': '하연', 'm_2020': '이도'}
    '''
