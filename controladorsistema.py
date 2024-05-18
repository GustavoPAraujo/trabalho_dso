from telasistema import TelaSistema
from controladormusica import ControladorMusica
from controladorusuario import ControladorUsuario

class ControladorSistema():

    def __init__(self) -> None:
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_musica = ControladorMusica(self)
        self.__tela_sistema = TelaSistema(self)
    @property
    def controlador_usuario(self):
        return self.__controlador_musica

    @property
    def controlador_musica(self):
        return self.__controlador_musica
    
    def inicia_sistema(self):
        self.abre_tela()

    def cadastra_usuario(self):
        self.__controlador_usuario.abre_tela()
    
    def cadastra_musica(self):
        self.__controlador_musica.abre_tela()
    

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuario, 2:self.cadastra_musica}

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()