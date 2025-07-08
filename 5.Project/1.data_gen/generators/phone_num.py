import random

class PhonenumGenerator:
    def generate(self):
        return f"050-{random.randint(10,9999):04d}-{random.randint(10,9999):04d}"