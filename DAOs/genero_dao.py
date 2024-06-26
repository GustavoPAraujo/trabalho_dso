from DAOs.dao import DAO
from entidades.genero import Genero


class GeneroDAO(DAO):
    def __init__(self):
        super().__init__('genero.pkl')

    def add(self, genero: Genero):
        super().add(genero.genero, genero)  # Usa o nome do gênero como chave

    def get(self, genero_nome: str):
        return super().get(genero_nome)

    def remove(self, genero_nome: str):
        super().remove(genero_nome)

