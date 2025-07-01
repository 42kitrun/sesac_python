import sys
from generators.user_generator import UserGen



# 최종실행
# print(sys.argv) # 입력 인자
# sys.argv[0] # 여기는 실행 파일명 자신
# sys.argv[1] # 첫번째 인자

if len(sys.argv) > 1:
    num_data = int(sys.argv[1])
else:
    num_data = int(input('원하는 데이터 갯수를 입력하시오: '))

    

my_data = DisplayData()
my_data.print_data(num_data)