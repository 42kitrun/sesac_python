import random

class AddressGenerator:
    # def __init__(self):
        # self.cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
        
    def __init__(self, file_path):
        self.__file_path = file_path

    def generate_address(self):
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            l_area, m_area, s_area = self.check_address([line.strip().split(',') for line in file.readlines()])

        return f'{l_area} {m_area} {s_area} {random.randint(1, 350)}'
    
    def check_address(self, array):
        l,m,s= array
        l_area = random.choice(l)
        m_area = random.choice(m)

        while l_area:# random.choice(l) 값이 있으면 true
            if l_area.endswith('시') and ('시' in m_area or m_area.endswith('군')):
                l_area = random.choice(l)
                m_area = random.choice(m)
                continue
            elif l_area.endswith('도') and ('시' not in m_area and m_area.endswith('구')):
                l_area = random.choice(l)
                m_area = random.choice(m)
                continue
            else:
                break
        
        return l_area, m_area, random.choice(s)