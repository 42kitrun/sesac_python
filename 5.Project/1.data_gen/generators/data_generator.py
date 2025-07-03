from user_generator import UserGenerator
from store_generator import StoreGenerator
from item_generator import ItemGenerator
from order_generator import OrderGenerator
from order_item_generator import OrderItemGenerator

            
def generate_data(_type, count):
    data = []

    if _type == 'user':
        data = UserGenerator().generate_user(count)
    elif _type == 'store':
        data = StoreGenerator().generate_store(count)
    elif _type == 'item':
        data = ItemGenerator().generate_item(count) # default 값은 0이고 전체 메뉴를 가져온다
    elif _type == 'order':
        data = OrderGenerator().generate_order(count)
    elif _type == 'orderitem':
        data = OrderItemGenerator().generate_order_items(count)
    else:
        raise Exception('유효하지 않은 유형입니다. \n user / store / item / order / orderitem 중에서 첫번째 인자를 입력하세요')
    
    return data


if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    # print(generate_data('orderitem',2))
    print(generate_data('order',2))

## orderitem
'''
Id,OrderAt,StoreId,UserId
f8d2e618-ab11-439f-a321-b0593f7f70ec,2025-07-02 23:25:05,8569d76f-cfb2-472d-a235-525ac7d5a8ec,bbc5ee4e-592d-4eed-85a1-79baf7c398e6
'''