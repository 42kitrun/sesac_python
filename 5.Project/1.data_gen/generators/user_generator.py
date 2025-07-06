from generators.generator import GenerateData
from generators.id import IdGenerator
from generators.name import NameGenerator
from generators.birthdate import BirthdateGenerator
from generators.gender import GenderGenerator
from generators.address import AddressGenerator
from generators.coordiate import CoordGenerator
from generators.phone_num import PhonenumGenerator

class UserGenerator:
    def __init__(self):
        self.__header = ['Id', 'Name', 'Gender', 'Age', 'Birthdate', 'Address','Coord','Phone_number']
        # 초기 객체를 불러올때는 처음 한번에 큰 데이터 가져오기
        self.generator_map = {
            'Id': IdGenerator(),
            'Name': NameGenerator('5.Project/1.data_gen/data/names.txt'),
            'Gender':GenderGenerator(),
            'Birthdate':BirthdateGenerator(),
            'Address':AddressGenerator('5.Project/1.data_gen/data/address_data.txt'),
            'Coord':CoordGenerator(),
            'Phone_number':PhonenumGenerator()
        }
        
        '''
        self.__header = ['Id', 'Name', 'Gender', 'Age', 'Birthdate', 'Address','Coord','Phone_number']
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator('5.Project/1.data_gen/data/names.txt')
        self.gender_gen = GenderGenerator()
        # self.age
        self.bday_gen = BirthdateGenerator()
        self.address_gen = AddressGenerator('5.Project/1.data_gen/data/address_data.txt')
        self.coord_gen = CoordGenerator()
        self.phone_gen = PhonenumGenerator()
        '''

    def generate(self, count:int)->tuple:
        users = []
  
        for _ in range(count):
            id = GenerateData(self.generator_map['Id'])()
            gender = GenerateData(self.generator_map['Gender'])()
            bday, age = GenerateData(self.generator_map['Birthdate'])() # bday에 따른 나이 계산
            dic_name = GenerateData(self.generator_map['Name'])() # gender와 bday에 따른 작명
            name = dic_name['sung'] + dic_name[f'{gender[0].lower()}_{bday[:3]}0']
            address = GenerateData(self.generator_map['Address'])()
            coord = GenerateData(self.generator_map['Coord'])()
            phone_num = GenerateData(self.generator_map['Phone_number'])()

            users.append((id, name, gender, age, bday, address, coord, phone_num))
            
        return (self.__header,users)
        '''[(UUID('48827553-1399-4488-9c1c-a667f6255788'), '구도준', 'Male', 1, '2023-11-16', '서울특별시 담양군 신남안길187번길 231')
          , (UUID('d1c52ffa-2b99-47e3-ae0a-d52012dd15fd'), '여서라', 'Female', 34, '1991-06-16', '경상남도 남양주시 선감로 196')]
        '''

if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(GenerateData(UserGenerator(),2)())        