from tela.telasistema import TelaSistema
from controle.controladormusica import ControladorMusica
from controle.controladorusuario import ControladorUsuario
from controle.controladorartista import ControladorArtista
from controle.controladorgenero import ControladorGenero
from controle.controladorplaylist import ControladorPlaylist
from entidades.recomendacao import Recomendacao


class ControladorSistema():

    def __init__(self) -> None:
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_musica = ControladorMusica(self)
        self.__controlador_artista = ControladorArtista(self)
        self.__controlador_genero = ControladorGenero(self)
        self.__controlador_platlist = ControladorPlaylist(self)
        self.__recomendacao = Recomendacao(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_usuario(self):
        return self.__controlador_musica

    @property
    def controlador_musica(self):
        return self.__controlador_musica

    @property
    def controlador_artista(self):
        return self.__controlador_artista

    @property
    def controlador_genero(self):
        return self.__controlador_genero

    @property
    def controlador_platlist(self):
        return self.__controlador_platlist

    @property
    def recomendacao(self):
        return self.__recomendacao

    def inicia_sistema(self):
        self.abre_tela()

    def cadastra_usuario(self):
        self.__controlador_usuario.abre_tela()

    def cadastra_musica(self):
        self.__controlador_musica.abre_tela()

    def cadastra_artista(self):
        self.__controlador_artista.abre_tela()

    def cadastra_genero(self):
        self.__controlador_genero.abre_tela()

    def cadastra_playlist(self):
        self.__controlador_platlist.abre_tela()

    def gera_recomendacao(self):
        self.__recomendacao.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuario,
                        2: self.cadastra_musica,
                        3: self.cadastra_artista,
                        4: self.cadastra_genero,
                        5: self.cadastra_playlist, 
                        6: self.gera_recomendacao,
                        7: self.encerra_sistema}

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            if opcao in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao]
                funcao_escolhida()