class Animal:
    def __init__(self, name: str) -> None:
        self._name = name
        self._energy:int = 100
        self._speak = ''
        self._move = 0

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def set_name(self,name:str)->None:
        self._name = name

    @property
    def energy(self) -> int:
        return self._energy
    
    @energy.setter
    def set_energy(self,energy:int)->None:
        self._energy = energy