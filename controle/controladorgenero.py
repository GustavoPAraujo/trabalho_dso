from DAOs.genero_dao import GeneroDAO
from entidades.genero import Genero
from tela.telagenero import TelaGenero

class ControladorGenero:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__genero_dao = GeneroDAO()
        self.__tela_genero = TelaGenero()

    def seleciona_genero(self, genero_musical):
        return self.__genero_dao.get(genero_musical.genero)

    def cadastra_genero(self):
        dados_genero = self.__tela_genero.criar_genero()
        novo_genero = Genero(dados_genero["genero"])

        if self.__genero_dao.get(novo_genero.genero) is None:
            self.__genero_dao.add(novo_genero.genero, novo_genero)
            self.__tela_genero.mostra_mnsg("Gênero cadastrado com sucesso!")
        else:
            self.__tela_genero.mostra_mnsg("Esse gênero já está cadastrado")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_genero, 2: self.retornar}

        while True:
            opcao = self.__tela_genero.tela_opcoes()
            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
