from entidades.artista import Artista
from entidades.genero import Genero
from uuid import uuid4

class Musica:
    def __init__(self, nome_musica: str, artista: Artista, genero: Genero) -> None:
        self.__id_musica = str(uuid4())
        self.__nome_musica = nome_musica
        self.__artista = artista
        self.__genero = genero

    @property
    def id_musica(self):
        return self.__id_musica

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
        if isinstance(artista, Artista):
            self.__artista = artista

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        if isinstance(genero, Genero):
            self.__genero = genero
