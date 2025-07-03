import uuid, csv
from datetime import datetime

class IdGenerator:
    uuid_history = set()
    '''한 번에 대량 생산시 중복여부 체크! 전체 생성 history를 구축하고 싶으면 파일이나 DB 사용해야함.
       파이썬 파일을 실행할 때마다 모든 변수, 클래스, 인스턴스, 클래스 변수 등은 힙 메모리에서 새로 만들어지기 때문에
       
       __로 시작하는 변수는 자식 클래스에서 접근이 어렵다!
       클래스 변수는 public(uuid_history) 또는 protected(_uuid_history)로 선언해서 상속 구조에서 공유'''
    
    # @classmethod
    # cls를 첫 번째 인자로 받아 메서드를 정의하여 클래스 변수 등에 접근할 수 있습니다
    @classmethod
    def generate_id(cls):
        id = uuid.uuid4()  # uuid는 16바이트로 고정! if 문자열로 변환하면 일반적으로 32~36바이트(하이픈 포함)
        while id in cls.uuid_history:# 무작위 생성이므로 중복 발생할 가능성 염두
            id = uuid.uuid4()
        cls.uuid_history.add(id)
        '''uuid로 보관하다가 사용시 문자열로 변환 안해도됨 :)
           문자열 <-> uuid 객체로 변환 str(uuid) <-> uuid.UUID(uuid_str)
        '''
        return id
    
    @classmethod
    def find_id_info(cls, _type, id) -> tuple:
        # 내부에서 생성한 id인지 여부
        if id in cls.uuid_history:
            print(f' -- 내부에서 생성한 id 입니다. {_type}.csv 에서 id를 찾습니다.')
        else:
            raise Exception(f"내부에서 생성한 id가 아닙니다. 발견일시 : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        with open(f'5.Project/1.data_gen/{_type}.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Id'] == id:
                    return tuple(row.values())
                
        print(f'유효하지 않은 id : {id}')
        return id,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'','' # 유효하지 않은 id, 유효하지 않음을 확인한 시각
    
## 주의 : 클래스를 정의하는 파일을 수행시 모든 값은 default 값으로 초기화 된다.
if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    # print(IdGenerator().generate_id())
    IdGenerator.uuid_history |= { # 혹은 .update({1,2,3})
'f8d2e618-ab11-439f-a321-b0593f7f70ec','ceb93608-e31c-4a16-826f-c516eff557a5',
'7440a665-dd0a-4393-a6db-0ff4f2893a0a','f8d2e618-ab11-439f-a321-b0593f7f70ec','1e30afde-8841-49c3-9a31-f82575da956b'
'9c425620-eee8-4177-a172-9c41689ab123','f8d2e618-ab11-439f-a321-b0593f7f70ec','a7e7b713-f7d0-410e-9017-ff5a2101a71f'
'bb880888-1b70-4a68-9f7c-6cbff253a560','f8d2e618-ab11-439f-a321-b0593f7f70ec','c0868b45-43b1-4d28-b74d-6a9518428ae5'
'8569d76f-cfb2-472d-a235-525ac7d5a8ec','bbc5ee4e-592d-4eed-85a1-79baf7c398e6'
    }
    print(IdGenerator.uuid_history)


    