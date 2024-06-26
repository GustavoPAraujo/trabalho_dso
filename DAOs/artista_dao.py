from DAOs.dao import DAO
from entidades.artista import Artista

class ArtistaDAO(DAO):
    def __init__(self):
        super().__init__('artista.pkl')

    def add(self, key: str, artista: Artista): # type: ignore
        super().add(key, artista.nome_artistico)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        super().remove(key)
