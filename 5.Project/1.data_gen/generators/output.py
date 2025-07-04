from data_generator import generate_data
import pandas as pd
import os, sys
import csv

import os



class DisplayData():
    def __init__(self):
        self.__header = []
        
    def generate_display(self,_type, count, display):
        # argv 체크
        if _type not in ['user','store','item','order','orderitem']:
            raise Exception('>>> user/store/item/order/orderitem 만 생성 가능합니다.')
        
        if display not in ['console','csv','excel']:
            raise Exception('>>> console/csv/excel 만 생성 가능합니다.')
        
        # 데이터 생성
        self.__header, data = generate_data(_type, count)

        # 데이터 출력
        {'console':self.print_console(_type,data)
         ,'csv':self.save_csv(_type,data)
         ,'excel':self.save_excel(_type,data)}[display]

    def print_console(self,_type, data):

        print( _type, ' 데이터 ',len(data), '개 목록')
        for row in data:
            for head, content in zip(self.__header,row):
                print(f"{head}: {content}")
            print()
        print(f"{_type} 출력 완료")
 

    def save_csv(self,_type, data):
        path = f'5.Project/1.data_gen/{_type}1.csv'
        
        # with open r+ 모드는 파일이 존재하지 않으면 에러
        if not os.path.exists(path):
            with open(path, 'a') as csvfile:
                csv_writer = csv.writer(csvfile)
        # 내용 쓰기
        with open(path, 'r+') as csvfile:
            csv_writer = csv.writer(csvfile)
            if not csvfile.read(2): # 앞에 두글자가 없으면 비어있는 파일로 판단하여 헤더 추가
                csv_writer.writerow(self.__header)
            csv_writer.writerows(data)
        print(f"{_type}.csv 파일에 {_type} 저장 완료")

    def save_excel(self,_type, data):
        df = pd.DataFrame(data, columns=self.__header)
        df.head()
        df.to_excel(f'5.Project/1.data_gen/{_type}.xlsx', index=False)
        print(f"{_type}.excel 파일에 {_type} 저장 완료")


if __name__ == '__main__':
    _type = ''
    num_data = ''
    display = ''
    input_info = "아래와 같이 공백으로 간격을 두어 입력하세요\n user 10_000 csv\n[user/store/item/order/orderitem] [데이터 갯수] [console/csv/excel] "

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