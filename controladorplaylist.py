from playlist import PlayList
from telaplaylist import TelaPlaylist

class ControladorPlaylist:
    def __init__(self) -> None:
        self.__lista_playlist = [PlayList]
        self.__tela_playlist = TelaPlaylist()
    
    def adicionar_playlist_in_playlists(self, playlist):
        if isinstance(playlist, PlayList):
            self.__lista_playlist.append(PlayList)
        return self.__lista_playlist
    