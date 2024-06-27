from DAOs.dao import DAO
from entidades.musica import Musica

class MusicaDAO(DAO):
    def __init__(self):
        super().__init__('musica.pkl')

    def add(self, key: str, musica: Musica): # type: ignore
        super().add(musica.id_musica, musica)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        super().remove(key)

    def get_all(self):
        return super().get_all()
    
    def listar_musicas(self):
        musicas = self.get_all()
        for musica in musicas:
            print(vars(musica))
