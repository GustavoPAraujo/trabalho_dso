
class Genero:
    def __init__(self, genero: str) -> None:
        if isinstance(genero, str):
            self.__genero = genero
    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        if isinstance(genero, str):
            self.__genero = genero