from pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome: str, nome_usuario: str, endereco_email: str, telefone: str):
        super().__init__(nome)
        if isinstance(nome_usuario, str):
            self.__nome_usuario = nome_usuario
        if isinstance(endereco_email, str):
            self.__endereco_email = endereco_email
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
    def endereco_email(self):
        return self.__endereco_email

    @endereco_email.setter
    def endereco_email(self, endereco_email):
        if isinstance(endereco_email, str):
            self.__endereco_email = endereco_email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        if isinstance(telefone, str):
            self.__telefone = telefone
