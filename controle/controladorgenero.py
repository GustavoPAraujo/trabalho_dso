from typing import List
from entidades.genero import Genero
from tela.telagenero import TelaGenero


class ControladorGenero:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_generos: List[Genero] = list()
        self.__tela_genero = TelaGenero()

    def seleciona_genero(self, genero_musical):
        genero_musical = Genero(genero_musical)
        for genero in self.__lista_generos:
            if genero.genero == genero_musical.genero:
                return genero

    def cadastra_genero(self):
        dados_genero = self.__tela_genero.criar_genero()
        novo_genero = Genero(dados_genero["genero"])

        nomes_generos = [genero.genero for genero in self.__lista_generos]
        if novo_genero.genero not in nomes_generos:
            self.__lista_generos.append(novo_genero)
            self.__tela_genero.mostra_mnsg("")
            self.__tela_genero.mostra_mnsg("Genero cadastrado coms sucesso!")
            self.__tela_genero.mostra_mnsg("")
        else:
            self.__tela_genero.mostra_mnsg("")
            self.__tela_genero.mostra_mnsg("Esse genero ja esta cadastrado")
            self.__tela_genero.mostra_mnsg("")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_genero, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_genero.tela_opcoes()]()
