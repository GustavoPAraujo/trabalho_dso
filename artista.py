from pessoa import Pessoa


class Artista(Pessoa):
    def __init__(self, nome: str, nome_artistico: str) -> None:
        super().__init__(nome)
        if isinstance(nome_artistico, str):
            self.__nome_artistico = nome_artistico
    
    @property
    def nome_artistico(self):
        return self.__nome_artistico
    
    @nome_artistico.setter
    def nome_artistico(self, nome_artistico):
        if isinstance(nome_artistico, str):
            self.__nome_artistico = nome_artistico
            