from animal import Animal

class Panda(Animal):
    sound = 'Pang~~Pang~~'

    def __init__(self,name):
        super().__init__(name)
        self._speak = 'Pang~~Pang~~'
        self._shrink_energy = 15
    
    def speak(self):
        return super().speak()
    
    def move(self):
        return super().move()