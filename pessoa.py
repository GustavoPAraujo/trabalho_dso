from abc import abstractmethod, ABC


class Pessoa(ABC):
    def __init__(self, nome: str) -> None:
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        # comentario
