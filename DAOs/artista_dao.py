from DAOs.dao import DAO
from entidades.artista import Artista

class ArtistaDAO(DAO):
    def __init__(self):
        super().__init__('artista.pkl')

    def add(self, key, artista: Artista): # type: ignore
        super().add(key, artista)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        super().remove(key)
