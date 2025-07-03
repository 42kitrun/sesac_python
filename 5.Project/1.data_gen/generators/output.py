from data_generator import generate_data
import sys
import csv

class DisplayData():
    def __init__(self):
        self.__header = {'user':['Id', 'Name', 'Gender', 'Age', 'Birthdate', 'Address']
                        ,'store':['Id','Name','Type','Address']
                        ,'item':['Id','Name','Type','UnitPrice']
                        ,'order':['Id','OrderAt','StoreId','UserId']
                        ,'orderitem':['Id','OrderId','ItemId']}
        
    def generate_display(self,_type, count, display):
        # 데이터 생성
        data = generate_data(_type, count)

        # 데이터 출력
        if display == 'console':
            self.print_console(_type,data)
        elif display == 'csv':
            self.save_csv(_type,data)
        else:
            raise Exception("지원되지 않는 출력 형태입니다.")

    def print_console(self,_type, data):
        for row in data:
            for head, content in zip(self.__header[_type],row):
                print(f"{head}: {content}")
            print()

    def save_csv(self,_type, data):
        if _type not in ['user','store','item','order','orderitem']:
            raise Exception('user/store/item/order/orderitem 만 생성 가능합니다.')

        with open(f'5.Project/1.data_gen/{_type}.csv', 'r+') as csvfile:
            csv_writer = csv.writer(csvfile)
            if not csvfile.read(2): # 앞에 한글자가 없으면 비어있는 파일로 판단하여 헤더 추가
                csv_writer.writerow(self.__header[_type])
            csv_writer.writerows(data)
        print(f"{_type}.csv 파일에 {_type} 저장 완료")

if __name__ == '__main__':
    _type = ''
    num_data = ''
    display = ''
    input_info = "아래와 같이 공백으로 간격을 두어 입력하세요\n user 10_000 csv\n[user/store/item/order/orderitem] [데이터 갯수] [console/csv] "

    argv_len = len(sys.argv)
    if argv_len  == 1: 
        try:
            _type, num_data, display = [e for e in input(input_info).strip().split(' ') if e] 
        except:
            raise Exception(input_info)
    elif argv_len == 4:
        _type, num_data, display = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        raise Exception(input_info)    

    num_data = int(num_data)
    my_data = DisplayData().generate_display(_type, num_data, display)