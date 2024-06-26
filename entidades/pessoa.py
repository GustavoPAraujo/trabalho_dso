from abc import abstractmethod, ABC


class Pessoa(ABC):
    def __init__(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
