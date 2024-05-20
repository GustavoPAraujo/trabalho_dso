from typing import List
from artista import Artista
from musica import Musica
from telamusica import TelaMusica


class ControladorMusica:
    def __init__(self, controlador_sistema) -> None:
        self.__lista_musicas: List[Musica] = list()
        self.__tela_musica = TelaMusica()
        self.__controlador_sistema = controlador_sistema

    def adicionar_musica(self):
        dados_musica = self.__tela_musica.pega_dados_musica()
        artista: Artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(dados_musica["artista"])
        genero = self.__controlador_sistema.controlador_genero.seleciona_genero(dados_musica["genero"])

        nova_musica = Musica(
            dados_musica["nome_musica"], artista, genero) # type: ignore

        if nova_musica not in self.__lista_musicas:
            self.__lista_musicas.append(nova_musica)
            self.__tela_musica.mostra_mnsg("Musica criada com sucesso!")

    def listar_musicas(self):
        for musica in self.__lista_musicas:
            genero = musica.genero.genero
            artista = musica.artista.nome_artistico
            
            self.__tela_musica.mostra_musica({"nome_musica": musica.nome_musica, "artista": artista, "genero": genero})


    def listar_musicas_por_genero(self):
        pega_genero = self.__tela_musica.selecionar_genero()
        genero = self.__controlador_sistema.controlador_genero.seleciona_genero(pega_genero)
        #verifica se o genero existe
        if genero is None:
            self.__tela_musica.mostra_mnsg("Não temos musicas com esse Gênero")
            return
        #adiciona as musicas do genero em uma lista
        musicas_do_genero: List[Musica] = []
        for musica in self.__lista_musicas:
            if genero == musica.genero:
                musicas_do_genero.append(musica)
        #mensagem de erro para falta de musicas do genero
        if not musicas_do_genero:
            self.__tela_musica.mostra_mnsg("Não temos musicas com esse Gênero")
        #lista musicas do genero
        for musica in musicas_do_genero:
            artista = musica.artista.nome_artistico
            genero = musica.genero.genero
            self.__tela_musica.mostra_musica({"nome_musica": musica.nome_musica, "artista": artista, "genero": genero})

    def pega_musica_genero(self):
        pega_genero = self.__tela_musica.selecionar_genero()
        genero = self.__controlador_sistema.controlador_genero.seleciona_genero(pega_genero)
        #verifica se o genero existe
        if genero is None:
            self.__tela_musica.mostra_mnsg("Não temos musicas com esse Gênero")
            return
        #adiciona as musicas do genero em uma lista
        musicas_do_genero: List[Musica] = []
        for musica in self.__lista_musicas:
            if genero == musica.genero:
                musicas_do_genero.append(musica)
        #mensagem de erro para falta de musicas do genero
        if not musicas_do_genero:
            self.__tela_musica.mostra_mnsg("Não temos musicas com esse Gênero")
        return musicas_do_genero

    def listar_musicas_por_artista(self):
        pega_artista = self.__tela_musica.seleciona_artista()
        artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(pega_artista)
        #verifica se o artista existe
        if artista is None:
            self.__tela_musica.mostra_mnsg("Não temos esse artista em nosso catalogo")
        #adiciona as musicas do artista em uma lista
        musicas_do_artista: List[Musica] = []
        for musica in self.__lista_musicas:
            if artista == musica.artista:
                musicas_do_artista.append(musica)
        #mensagem de erro para falta de musicas do artista
        if not musicas_do_artista:
            self.__tela_musica.mostra_mnsg("Não temos musicas desse Artista")
        #lista musicas do artista
        for musica in musicas_do_artista:
            artista = musica.artista.nome_artistico
            genero = musica.genero.genero
            self.__tela_musica.mostra_musica({"nome_musica": musica.nome_musica, "artista": artista, "genero": genero})

    def pega_musica_artista(self):
        pega_artista = self.__tela_musica.seleciona_artista()
        artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(pega_artista)
        #verifica se o artista existe
        if artista is None:
            self.__tela_musica.mostra_mnsg("Não temos esse artista em nosso catalogo")
        #adiciona as musicas do artista em uma lista
        musicas_do_artista: List[Musica] = []
        for musica in self.__lista_musicas:
            if artista == musica.artista:
                musicas_do_artista.append(musica)
        #mensagem de erro para falta de musicas do artista
        if not musicas_do_artista:
            self.__tela_musica.mostra_mnsg("Não temos musicas desse Artista")
        return musicas_do_artista

    def verificar_musica(self, nome_musica, artista, genero):
        verificar_artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(artista)
        verificar_genero = self.__controlador_sistema.controlador_genero.seleciona_genero(genero)
        musica_verificar = Musica(nome_musica, verificar_artista, verificar_genero)
        if musica_verificar in self.__lista_musicas:
            return musica_verificar

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_musica, 2: self.listar_musicas,
                        3: self.listar_musicas_por_genero, 4: self.listar_musicas_por_artista, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_musica.tela_opcoes()]()
