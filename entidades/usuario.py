from entidades.pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome: str, nome_usuario: str, email: str, telefone: str):
        super().__init__(nome)
        if isinstance(nome_usuario, str):
            self.__nome_usuario = nome_usuario
        if isinstance(email, str):
            self.__email = email
        if isinstance(telefone, str):
            self.__telefone = telefone
        self.__musicas_preferidas = []
        self.__amizades = []

    @property
    def nome_usuario(self):
        return self.__nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, nome_usuario):
        if isinstance(nome_usuario, str):
            self.__nome_usuario = nome_usuario

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if isinstance(email, str):
            self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        if isinstance(telefone, str):
            self.__telefone = telefone
    
    @property
    def musicas_preferidas(self):
        return self.__musicas_preferidas
    
    @property
    def amizades(self):
        return self.__amizades
