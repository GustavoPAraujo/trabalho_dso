from telasistema import TelaSistema
from controladormusica import ControladorMusica
from controladorusuario import ControladorUsuario
from controladorartista import ControladorArtista
from controladorgenero import ControladorGenero
from controladorplaylist import ControladorPlaylist
from recomendacao import Recomendacao


class ControladorSistema():

    def __init__(self) -> None:
        self.__recomendacao = Recomendacao(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_musica = ControladorMusica(self)
        self.__controlador_artista = ControladorArtista(self)
        self.__controlador_genero = ControladorGenero(self)
        self.__controlador_platlist = ControladorPlaylist(self)
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
        return self.__controlador_playlist
    
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

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuario, 2: self.cadastra_musica,
                        3: self.cadastra_artista, 4: self.cadastra_genero, 5: self.cadastra_playlist, 6: self.gera_recomendacao}

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
