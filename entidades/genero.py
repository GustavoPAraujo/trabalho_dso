
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

    def __eq__(self, other):
        if isinstance(other, Genero):
            return self.genero == other.genero
        return False

    def __hash__(self):
        return hash(self.genero)
