import random

class NameGenerator:
    # def __init__(self) -> None:
    #     # 기존 하드코딩 되어 있던걸, 파일을 통해 읽는 방식으로 변경해보기
    #     self.names = ['James','Jane','Michael','Emily','William','Olivia']
    def __init__(self, file_path) -> None:
        self.names = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r') as file:
            data = file.read().splitlines

    def generate_name(self):
        return random.choice(self.names)

class BirthdateGenerator:
    def generate_birthdate(self):
        year = random.randint(1990, 2010)
        month = random.randint(1, 12)
        day = random.randint(1,28)
        return f"{year}-{month:02d}-{day:02d}"

class GenderGenerator:
    def generate_gender(self):
        return random.choice(['Female','Male'])
    
class UserGenerator:
    def __init__(self):
        self.name_gen = NameGenerator('names.txt')
        self.bday_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()

class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for name, birthdate, gender, address in data :
            print(f"Name: {name}\n")