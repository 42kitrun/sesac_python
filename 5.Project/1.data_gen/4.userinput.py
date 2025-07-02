import sys
import csv
from generators.user_generator import UserGenerator

class DisplayData(UserGenerator):

    def print_console(self, count):
        data = self.generate_user(count)
        for id, name, gender, age, bday, address in data:
            print(f"id: {id} Name: {name} Gender: {gender} age: {age}  Birthdate: {bday}  Address: {address}")

    def print_csv(self, count):
        data = self.generate_user(count)
        with open('5.Project/1.data_gen/user.csv', 'w') as file:
            csv_writer = csv.writer(file)
            
            csv_writer.writerow(['Id', 'Name', 'Gender', 'Age', 'Birthdate', 'Address'])
            csv_writer.writerows(data)
            
        print(f"CSV 파일에 저장 완료")

# 최종 실행
# print(sys.argv)  # 입력 인자
# sys.argv[0] # 여기는 실행 파일명 자신
# sys.argv[1] # 첫번째 인자

if len(sys.argv) > 1: 
    num_data = int(sys.argv[1])
else:
    num_data = int(input("원하는 데이터 갯수를 입력하시오: "))

output_format = 'console'
if len(sys.argv) > 2:
    output_format = sys.argv[2]

my_data = DisplayData()
if output_format == 'console':
    my_data.print_console(num_data)
elif output_format == 'csv':
    my_data.print_csv(num_data)
else:
    print("지원되지 않는 출력 형태입니다.")