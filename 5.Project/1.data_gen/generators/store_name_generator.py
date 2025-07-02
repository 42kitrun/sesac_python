import random

class StoreNameGenerator:
    def __init__(self, file_path):
        self.__file_path = file_path

    def generate_store_name(self):
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            b,l,t = [line.strip().split(',') for line in file.readlines()]

        return random.choice(b), random.choice(l)+random.choice(t)

print(StoreNameGenerator('5.Project/1.data_gen/store_names.txt').generate_store_name())