import random

class StoreNameGenerator:
    def __init__(self, file_path):
        self.__file_path = file_path

    def generate(self):
        # 기초데이터는 지하철 역명(공공데이터)과 스타벅스 지점명(위키) 활용
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            b,l,t = [line.strip().split(',') for line in file.readlines()]

        return random.choice(b), f'{random.choice(l)}{random.choice(t)}'
    
## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(StoreNameGenerator('5.Project/1.data_gen/data/store_names.txt').generate())