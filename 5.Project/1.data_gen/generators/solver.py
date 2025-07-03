from user_generator import UserGenerator
from store_generator import StoreGenerator
from item_generator import ItemGenerator

from random import choice, randint
import csv

def select_id(_type:str):
    with open(f'5.Project/1.data_gen/{_type}.csv', 'r') as csvfile:
        # 파일 내용 불러오기
        csv_reader = csv.DictReader(csvfile)
        csv_list = list(csv_reader)

        # 유형에 따라 id 불러오기
        if _type in ['user','store','item','order']:
            return choice(csv_list)["Id"]
        elif _type == 'orderitem':
            return [choice(csv_list)["Id"] for _ in range(randint(1,8))]
        else: raise Exception('유효하지 않은 유형입니다. [user / store / item / order / orderitem]')
'''
def verify_id_info(_type, id) -> tuple:
        with open(f'5.Project/1.data_gen/{_type}.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            return tuple([ row.values() for row in csv_reader if row['Id'] == id])
                
        print(f'유효하지 않은 id : {id}')
        return id,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'','' # 유효하지 않은 id, 유효하지 않음을 확인한 시각
'''             
def generate_data(_type, count):
    data = []

    if _type == 'user':
        data = UserGenerator().generate_user(count)
    elif _type == 'store':
        data = StoreGenerator().generate_store(count)
    elif _type == 'item':
        data = ItemGenerator().generate_item(count) # default 값은 0이고 전체 메뉴를 가져온다
    else:
        raise Exception('유효하지 않은 유형입니다. \n user / store / item 중에서 첫번째 인자를 입력하세요')
    
    return data


if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(generate_data('user',2))

## orderitem
'''
Id,OrderAt,StoreId,UserId
f8d2e618-ab11-439f-a321-b0593f7f70ec,2025-07-02 23:25:05,8569d76f-cfb2-472d-a235-525ac7d5a8ec,bbc5ee4e-592d-4eed-85a1-79baf7c398e6
'''