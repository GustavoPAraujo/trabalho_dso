from musica import Musica
from usuario import Usuario


class PlayList:
    def __init__(self, musica: Musica, nome_playlist):
        self.__playlist = list()
        self.__nome_playlist = nome_playlist
        self.__musica = musica

    @property
    def nome_playlist(self):
        return self.__nome_playlist
    
    @nome_playlist.setter
    def nome_playlist(self, nome_playlist):
        self.__nome_playlist = nome_playlist
    
    def adicionar_musica_playlist(self, musica: Musica):
        if isinstance(musica,Musica):
            self.__playlist.append(musica)
        return self.__playlist
    
    def excluir_musica(self, musica: Musica):
        if isinstance(musica, Musica):
            self.__playlist.remove(Musica)
        return self.__playlist
    