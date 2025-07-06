from datetime import datetime, date
import random

class BirthdateGenerator:
    def generate(self):
        year = random.randint(1960, 2024)
        month = random.randint(1, 12)
        day = random.randint(1, 28)

        ymd = f"{year}-{month:02d}-{day:02d}"
        return ymd, int((date.today() - datetime.strptime(ymd, '%Y-%m-%d').date()).days/365.25) #지구가 태양을 한 바퀴 도는 공전 주기 대략 365.25
        
    

    