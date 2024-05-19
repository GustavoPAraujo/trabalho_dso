from artista import Artista
from genero import Genero


class Musica:
    def __init__(self, nome_musica: str, artista: str, genero: str) -> None:
        if isinstance(nome_musica, str):
            self.__nome_musica = nome_musica
        if isinstance(artista, str):
            self.__artista = artista
        if isinstance(genero, str):
            self.__genero = genero

    @property
    def nome_musica(self):
        return self.__nome_musica

    @nome_musica.setter
    def nome_musica(self, nome_musica):
        if isinstance(nome_musica, str):
            self.__nome_musica = nome_musica

    @property
    def artista(self):
        return self.__artista

    @artista.setter
    def artista(self, artista):
        if isinstance(artista, str):
            self.__artista = artista

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        if isinstance(genero, str):
            self.__genero = genero
    
    def criar_musica(self, nome_musica, artista, genero):
        nova_musica = Musica(nome_musica, artista, genero)
        return nova_musica
