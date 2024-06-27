from entidades.artista import Artista
from tela.telaartista import TelaArtista
from DAOs.artista_dao import ArtistaDAO


class ControladorArtista:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_artista = TelaArtista()
        self.__artista_dao = ArtistaDAO()

    def pega_artista_por_nome(self, nome_artistico):
        artista = self.__artista_dao.get(nome_artistico)
        if artista is not None:
            return artista
        return None


    def cadastra_artista(self):
        dados_artista = self.__tela_artista.criar_artista()
        novo_artista = Artista(dados_artista["nome"], dados_artista["nome_artistico"])

        if self.__artista_dao.get(novo_artista.nome_artistico) is None:
            self.__artista_dao.add(novo_artista.nome_artistico, novo_artista)
            self.__tela_artista.mostra_mnsg("Artista cadastrado com sucesso!")
        else:
            self.__tela_artista.mostra_mnsg("Um artista com esse nome já está cadastrado")


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_artista, 2: self.retornar}

        while True:
            lista_opcoes[self.__tela_artista.tela_opcoes()]()
