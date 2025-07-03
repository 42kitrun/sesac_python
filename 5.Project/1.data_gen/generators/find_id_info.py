from datetime import datetime
import csv

def find_id_info(_type, id) -> tuple:
        with open(f'5.Project/1.data_gen/{_type}.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Id'] == id:
                    return tuple(row.values())
                
        print(f'유효하지 않은 id : {id}')
        return id,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'','' # 유효하지 않은 id, 유효하지 않음을 확인한 시각


if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(find_id_info('order', id = 'f8d2e618-ab11-439f-a321-b0593f7f70ec'))

## orderitem
'''
Id,OrderAt,StoreId,UserId
f8d2e618-ab11-439f-a321-b0593f7f70ec,2025-07-02 23:25:05,8569d76f-cfb2-472d-a235-525ac7d5a8ec,bbc5ee4e-592d-4eed-85a1-79baf7c398e6
'''