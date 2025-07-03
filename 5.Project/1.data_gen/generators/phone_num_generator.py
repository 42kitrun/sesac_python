import random

class PhonenumGenerator:
    def generate_phone_num(self):
        return f"010-{random.randint(10,9999):04d}-{random.randint(10,9999):04d}"