import random

class CoordGenerator:
    def generate(self):
        return f'Lat: {random.uniform(33.0000, 43.9999):.4f}° Lng: {random.uniform(124.0000, 131.9999):.4f}°'
