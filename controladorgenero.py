from typing import List
from genero import Genero
from telagenero import TelaGenero


class ControladorGenero:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
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

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_genero, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_genero.tela_opcoes()]()

