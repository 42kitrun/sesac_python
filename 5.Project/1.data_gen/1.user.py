import random

names = ['James','Jane','Michael','Emily','William','Olivia']
cities = ['New York','Los Angeles','Chicago']

def generate_name():
    return random.choice(names)

def generate_birthdate():
    year = random.randint(1990, 2010)
    month = random.randint(1, 12)
    day = random.randint(1,28)
    return f"{year}-{month:02d}-{day:02d}"

def generate_gender():
    return random.choice(['Female','Male'])

def generate_address():
    city = random.choice(cities)
    street_num = random.randint(1,100)
    return f'{street_num} {cities}'

users=[]
for _ in range(10):
    name = generate_name()
    bday = generate_birthdate()
    users.append((name, bday))

for u in users:
    print(u)

print(generate_birthdate())

