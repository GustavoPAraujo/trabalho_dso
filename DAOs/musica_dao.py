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

    def get_by_genero(self, genero):
        return [musica for musica in self.get_all() if musica.genero == genero]

    def get_by_artista(self, artista):
        return [musica for musica in self.get_all() if musica.artista == artista]

    def get_by_details(self, nome_musica, artista, genero):
        for musica in self.get_all():
            if (musica.nome_musica == nome_musica and
                musica.artista == artista and
                musica.genero == genero):
                return musica
        return None