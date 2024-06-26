from DAOs.dao import DAO
from entidades.usuario import Usuario

class UsuarioDao(DAO):
    def __init__(self):
        super().__init__('usuario.pkl')

    def add(self, key: str, usuario: Usuario): # type: ignore
        super().add(key, usuario)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        super().remove(key)

    def get_all(self):
        return super().get_all()

    def update(self, key: str, usuario: Usuario):  # type: ignore 
        super().update(key, usuario)
