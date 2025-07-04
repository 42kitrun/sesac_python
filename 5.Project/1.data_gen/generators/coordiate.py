import random

class CoordGenerator:
    def generate(self):
        return f'''Lat: {random.randint(33,43)}° {random.randint(0,59):02d}'{random.randint(0,59):02d}" Lng: {random.randint(124,131)}° {random.randint(0,59):02d}'{random.randint(0,59):02d}"]'''
