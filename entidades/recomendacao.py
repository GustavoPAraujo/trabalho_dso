from tela.telarecomendacao import TelaRecomendacao
import random

class Recomendacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_recomendacao = TelaRecomendacao()

    def recomendacao_por_genero(self):
        musicas_genero = self.__controlador_sistema.controlador_musica.pega_musica_genero()

        if not musicas_genero:
            self.__tela_recomendacao.mostra_mnsg("Não há músicas disponíveis para o gênero selecionado.")
            return

        recomendacao_genero = random.choice(musicas_genero)
        return self.__tela_recomendacao.mostra_mnsg(f'{recomendacao_genero.nome_musica}')
    
    def recomendacao_por_artista(self):
        artista_escolhido = self.__tela_recomendacao.pega_artista()
        musicas_artista = self.__controlador_sistema.controlador_musica.pega_musica_artista(artista_escolhido)

        if not musicas_artista:
            self.__tela_recomendacao.mostra_mnsg("Não há músicas disponíveis para o artista selecionado.")
            return

        recomendacao_artista = random.choice(musicas_artista)
        return print(recomendacao_artista.nome_musica)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.recomendacao_por_genero, 2: self.recomendacao_por_artista,
                        3: self.retornar}

        while True:
            lista_opcoes[self.__tela_recomendacao.tela_opcoes()]()
