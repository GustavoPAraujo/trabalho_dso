from DAOs.dao import DAO
from entidades.usuario import Usuario

class UsuarioDao(DAO):
    def __init__(self):
        super().__init__('usuario.pkl')

    def add(self, key: str, usuario: Usuario): # type: ignore
        super().add(key, usuario.nome_usuario)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        super().remove(key)
