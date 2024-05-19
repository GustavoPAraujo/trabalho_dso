from typing import List
from artista import Artista
from telaartista import TelaArtista


class ControladorArtista:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__lista_artistas: List[Artista] = list()
        self.__tela_artista = TelaArtista()

    def pega_artista_por_nome(self, nome_artistico):
        for artista in self.__lista_artistas:
            if artista.nome_artistico == nome_artistico:
                return artista

    def cadastra_artista(self):
        dados_artista = self.__tela_artista.criar_artista()
        novo_artista = Artista(
            dados_artista["nome"], dados_artista["nome_artistico"])

        if novo_artista not in self.__lista_artistas:
            self.__lista_artistas.append(novo_artista)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_artista, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_artista.tela_opcoes()]()
