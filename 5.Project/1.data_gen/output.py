import sys
import csv
from generators.user_generator import UserGenerator
from generators.store_generator import StoreGenerator
from generators.item_generator import ItemGenerator

class DisplayData():
    def __init__(self):
        self.__header = {'user':['Id', 'Name', 'Gender', 'Age', 'Birthdate', 'Address']
                        ,'store':['Id','Name','Type','Address']
                        ,'item':['Id','Name','Type','UnitPrice']}
        
    def generate_data(self,_type, count):
        data = []
        if _type == 'user':
            data = UserGenerator().generate_user(count)
        elif _type == 'store':
            data = StoreGenerator().generate_store(count)
        elif _type == 'item':
            data = ItemGenerator().generate_item(count) # default 값은 0이고 전체 메뉴를 가져온다
        else:
            print('유효하지 않은 유형입니다. \n user / store / item 중에서 첫번째 인자를 입력하세요')
        
        return data
    
    def print_console(self,_type, count):
        data = self.generate_data(_type, count)
        for row in data:
            for head, content in zip(self.__header[_type],row):
                print(f"{head}: {content}")
            print()

    def print_csv(self,_type, count):
        data = self.generate_data(_type, count)
        with open(f'5.Project/1.data_gen/{_type}.csv', 'w') as file:
            csv_writer = csv.writer(file)
            
            csv_writer.writerow(self.__header[_type])
            csv_writer.writerows(data)
            
        print(f"CSV 파일에 저장 완료")

if __name__ == '__main__':
    _type = ''
    num_data = ''
    display = ''

    argv_len = len(sys.argv)
    if argv_len < 2: 
        _type, num_data, display = input("아래와 같이 공백으로 간격을 두어 입력하세요\nuser 10_000 csv\n[user/store/item] [데이터 갯수] [console/csv] ").split(' ')
    elif argv_len == 4:
        _type, num_data, display = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        print("아래와 같이 공백으로 간격을 두어 입력하세요\noutput.py user 10_000 csv\noutput.py [user/store/item] [데이터 갯수] [console/csv] ")    
        exit()

    num_data = int(num_data)
    my_data = DisplayData()
    if display == 'console':
        my_data.print_console(_type,num_data)
    elif display == 'csv':
        my_data.print_csv(_type,num_data)
    else:
        print("지원되지 않는 출력 형태입니다.")