from DAOs.dao import DAO
from entidades.genero import Genero

class GeneroDAO(DAO):
    def __init__(self):
        super().__init__('genero.pkl')

    def add(self, key: str, genero: Genero): # type: ignore
        super().add(key, genero)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        super().remove(key)
