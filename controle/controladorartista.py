from typing import List
from entidades.artista import Artista
from tela.telaartista import TelaArtista


class ControladorArtista:
    def __init__(self, controlador_sistema):
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

        nomes_artistas = [artista.nome_artistico for artista in self.__lista_artistas]
        if novo_artista.nome_artistico not in nomes_artistas:
            self.__lista_artistas.append(novo_artista)
            self.__tela_artista.mostra_mnsg("")
            self.__tela_artista.mostra_mnsg("Artista cadastrado com sucesso!")
            self.__tela_artista.mostra_mnsg("")
        else:
            self.__tela_artista.mostra_mnsg("")
            self.__tela_artista.mostra_mnsg("Escolha outro nome artistico")
            self.__tela_artista.mostra_mnsg("")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_artista, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_artista.tela_opcoes()]()
