from musica import Musica
from usuario import Usuario


class PlayList:
    def __init__(self, nome_playlist, musica: Musica):
        self.__playlist = list()
        self.__nome_playlist = nome_playlist
        self.__musica = musica
        self.__playlist.append(musica.nome_musica)

    @property
    def nome_playlist(self):
        return self.__nome_playlist
    
    @nome_playlist.setter
    def nome_playlist(self, nome_playlist):
        self.__nome_playlist = nome_playlist

    @property
    def musicas_playlist(self):
        return self.__playlist
    

    

    