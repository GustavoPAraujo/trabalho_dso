from DAOs.dao import DAO
from entidades.playlist import PlayList

class PlaylistDAO (DAO):
    def __init__(self):
        super().__init__('playlist.pkl')

    def add(self, key, playlist: PlayList): # type: ignore
        return super().add(playlist.__id_playlist, playlist)
    
    def get(self, key):
        return super().get(key)
    
    def remove(self, key):
        return super().remove(key)
    
    def get_all(self):
        return super().get_all()
    
    def listar_playlists(self):
        playlists = self.get_all()
        for playlist in playlists:
            print(vars(playlist))