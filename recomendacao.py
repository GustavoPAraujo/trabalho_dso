from telarecomendacao import TelaRecomendacao
import random

class Recomendacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_recomendacao = TelaRecomendacao()

    def recomendacao_por_genero(self):
        genero_escolhido = self.__tela_recomendacao.pega_genero()
        musicas_genero = self.__controlador_sistema.controlador_musica.pega_musica_genero(genero_escolhido)
        recomendacao_genero = random.choice(musicas_genero)
        return print(recomendacao_genero.nome_musica)
    
    def recomendacao_por_artista(self):
        artista_escolhido = self.__tela_recomendacao.pega_artista()
        musicas_artista = self.__controlador_sistema.controlador_musica.pega_musica_artista(artista_escolhido)
        recomendacao_artista = random.choice(musicas_artista)
        return print(recomendacao_artista.nome_musica)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.recomendacao_por_genero, 2: self.recomendacao_por_artista,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_recomendacao.tela_opcoes()]()
