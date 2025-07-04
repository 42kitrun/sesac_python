from id import IdGenerator
from name import NameGenerator
from birthdate import BirthdateGenerator
from gender import GenderGenerator
from address import AddressGenerator
from phone_num import PhonenumGenerator

from datetime import datetime, date



class UserGenerator:
    def __init__(self):
        self.id_map = {
            'Id': IdGenerator()
            , 'Name': NameGenerator('5.Project/1.data_gen/names.txt')
            , 'Gender': GenderGenerator()
            , 'Birthdate' : BirthdateGenerator()
            , 'Address_GPSCoord' : AddressGenerator('5.Project/1.data_gen/address_data.txt')
            ,'Phone_number' : PhonenumGenerator()
        }
        '''
        self.__header = ['Id', 'Name', 'Gender', 'Age', 'Birthdate', 'Address_GPSCoord','Phone_number']
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator('5.Project/1.data_gen/names.txt')
        self.gender_gen = GenderGenerator()
        # self.age
        self.bday_gen = BirthdateGenerator()
        self.address_gen = AddressGenerator('5.Project/1.data_gen/address_data.txt')
        self.phone_gen = PhonenumGenerator()
        '''

    def calculate_age(self, bday:str) -> int:
        '나이를 구하는 함수'
        # int : 소수점 버림
        return int((date.today() - datetime.strptime(bday, '%Y-%m-%d').date()).days/365.25) #지구가 태양을 한 바퀴 도는 공전 주기 대략 365.25
        
    def generate_user(self, count:int)->tuple:
        users = []
  
            

        '''
        for _ in range(count):
            id = self.id_gen.generate_id()
            gender = self.gender_gen.generate_gender()
            bday = self.bday_gen.generate_birthdate()
            dic_name = self.name_gen.generate_name() # gender와 bday에 따른 작명
            name = dic_name['sung'] + dic_name[f'{gender[0].lower()}_{bday[:3]}0']
            age = self.calculate_age(bday) # bday에 따른 나이 계산
            address = self.address_gen.generate_address()
            phone_num = self.phone_gen.generate_phone_num()
        '''
            users.append((id, name, gender, age, bday, address, phone_num))
            
        return (self.__header,users)
        '''[(UUID('48827553-1399-4488-9c1c-a667f6255788'), '구도준', 'Male', 1, '2023-11-16', '서울특별시 담양군 신남안길187번길 231')
          , (UUID('d1c52ffa-2b99-47e3-ae0a-d52012dd15fd'), '여서라', 'Female', 34, '1991-06-16', '경상남도 남양주시 선감로 196')]
        '''

if __name__ == '__main__': # 아래 스크립트는 본 파일을 직접 실행할 때만(module로 불러올때 말고)
    print(UserGenerator().generate_user(2))        