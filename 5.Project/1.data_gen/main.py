from generators.data_generator import generate_data
import pandas as pd
import os, sys
import csv

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
        if display == 'console':
            self.print_console(_type,data)
        elif display == 'csv':
            self.save_csv(_type,data)
        else:
            self.save_excel(_type,data)
        
        '''
        이 메소드에서는 되는데
        data_generator.generate_data(_type, count)
        왜 이 경우는 다같이 실행할까....ㅠㅠ
        dis = {'console':self.print_console(_type,data)
        ,'csv':self.save_csv(_type,data)
        ,'excel':self.save_excel(_type,data)
        }
        
        return dis[display]
        '''

    # Console 출력
    def print_console(self,_type, data):

        print( _type, ' 데이터 ',len(data), '개 목록')
        for row in data:
            for head, content in zip(self.__header,row):
                print(f"{head}: {content}")
            print()
        print(f"{_type} {display} 출력 완료")
 
    # csv 파일 저장
    def save_csv(self,_type, data):
        path = f'5.Project/1.data_gen/output/{_type}.csv'
        
        # with open r+ 모드는 파일이 존재하지 않으면 에러
        if not os.path.exists(path):
            with open(path, 'w') as csvfile:
                pass
        # 내용 쓰기
        with open(path, 'r+', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            csv_writer = csv.writer(csvfile)
            if not len(list(csv_reader)): # 앞에 두글자가 없으면 비어있는 파일로 판단하여 헤더 추가
                csv_writer.writerow(self.__header)
            csv_writer.writerows(data)
        print(f"{_type}.csv 파일에 {_type} 저장 완료")

    # excel 파일 저장
    def save_excel(self,_type, data):
        df = pd.DataFrame(data, columns=self.__header)
        df.head()
        df.to_excel(f'5.Project/1.data_gen/output/{_type}.xlsx', index=False)
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