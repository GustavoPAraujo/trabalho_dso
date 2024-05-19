
from genero import Genero
from telagenero import TelaGenero
from controladorsistema import ControladorSistema
from typing import List

class ControladorGenero:
    def __init__(self, controlador_sistema: ControladorSistema) -> None:
        self.__controlador_sistema: ControladorSistema = controlador_sistema
        self.__lista_generos: List[Genero] = list()
        self.__tela_genero = TelaGenero()

    def seleciona_genero(self, genero_musical):
        for genero in self.__lista_generos:
            if genero.genero == genero_musical:
                return genero 


    def cadastra_genero(self):
        dados_genero = self.__tela_genero.criar_genero()
        novo_genero = Genero(dados_genero["genero"])

        if novo_genero not in self.__lista_generos:
            self.__lista_generos.append(novo_genero)

#    def pega_artista_por_nome(self, nome_artistico) -> Artista | None:
#        for artista in self.__lista_artistas:
#            if artista.nome_artistico == nome_artistico:
#                return artista



    def abre_tela(self):

        lista_opcoes = {1: self.cadastra_genero}

        while True:
            lista_opcoes[self.__tela_genero.tela_opcoes()]()

