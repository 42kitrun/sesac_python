import random

class BirthdateGenerator:
    def generate(self):
        year = random.randint(1960, 2024)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"
    