from typing import List
from entidades.artista import Artista
from entidades.musica import Musica
from tela.telamusica import TelaMusica


class ControladorMusica:
    def __init__(self, controlador_sistema):
        self.__lista_musicas: List[Musica] = list()
        self.__tela_musica = TelaMusica()
        self.__controlador_sistema = controlador_sistema

    def adicionar_musica(self):
        dados_musica = self.__tela_musica.pega_dados_musica()

        artista: Artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(
            dados_musica["artista"])
        if artista is None:
            self.__tela_musica.mostra_mnsg("Artista não encontrado.")
            return
        
        genero = self.__controlador_sistema.controlador_genero.seleciona_genero(
            dados_musica["genero"])
        if genero is None:
            self.__tela_musica.mostra_mnsg("Gênero não encontrado.")
            return

        for musica in self.__lista_musicas:
            if (musica.nome_musica == dados_musica["nome_musica"] and
                musica.artista == artista and
                    musica.genero == genero):
                self.__tela_musica.mostra_mnsg("Essa música já está cadastrada.")

                return

        nova_musica = Musica(
            dados_musica["nome_musica"], artista, genero)

        self.__lista_musicas.append(nova_musica)

        self.__tela_musica.mostra_mnsg("Musica criada com sucesso!")


    def listar_musicas(self):
        if not self.__lista_musicas:
            self.__tela_musica.mostra_mnsg("Não temos musicas no momento")
            return
        
        n_musica = 1
        for musica in self.__lista_musicas:
            genero = musica.genero.genero
            artista = musica.artista.nome_artistico

            dados_musica = {"nome_musica": musica.nome_musica, "artista": artista, "genero": genero}
            self.__tela_musica.mostra_musica(n_musica , dados_musica)
            n_musica += 1

    def listar_musicas_por_genero(self):
        pega_genero = self.__tela_musica.selecionar_genero()
        genero = self.__controlador_sistema.controlador_genero.seleciona_genero(
            pega_genero)
        # verifica se o genero existe
        if genero is None:
            self.__tela_musica.mostra_mnsg("Não temos musicas com esse Gênero")

            return
        # adiciona as musicas do genero em uma lista
        musicas_do_genero: List[Musica] = []
        for musica in self.__lista_musicas:
            if genero == musica.genero:
                musicas_do_genero.append(musica)
        # mensagem de erro para falta de musicas do genero
        if not musicas_do_genero:
            self.__tela_musica.mostra_mnsg("Não temos musicas com esse Gênero")

        # lista musicas do genero
        for musica in musicas_do_genero:
            artista = musica.artista.nome_artistico
            genero = musica.genero.genero
            self.__tela_musica.mostra_musica(0,
                {"nome_musica": musica.nome_musica, "artista": artista, "genero": genero})

    def pega_musica_genero(self, genero_escolhido):
        genero = self.__controlador_sistema.controlador_genero.seleciona_genero(genero_escolhido)
        # verifica se o genero existe
        if genero is None:
            self.__tela_musica.mostra_mnsg("Não temos musicas com esse Gênero")
   
            return
        # adiciona as musicas do genero em uma lista
        musicas_do_genero: List[Musica] = []
        for musica in self.__lista_musicas:
            if genero == musica.genero:
                musicas_do_genero.append(musica)
        # mensagem de erro para falta de musicas do genero
        if not musicas_do_genero:
            self.__tela_musica.mostra_mnsg("Não temos musicas com esse Gênero")

        return musicas_do_genero

    def listar_musicas_por_artista(self):
        pega_artista = self.__tela_musica.seleciona_artista()
        artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(
            pega_artista)
        # verifica se o artista existe
        if artista is None:
            self.__tela_musica.mostra_mnsg(
                "Não temos esse artista em nosso catalogo")

            return
        # adiciona as musicas do artista em uma lista
        musicas_do_artista: List[Musica] = []
        for musica in self.__lista_musicas:
            if artista == musica.artista:
                musicas_do_artista.append(musica)
        # mensagem de erro para falta de musicas do artista
        if not musicas_do_artista:
            self.__tela_musica.mostra_mnsg("Não temos musicas desse Artista")

            return
        # lista musicas do artista
        self.__tela_musica.mostra_mnsg("Musicas de: {artista}")
        for musica in musicas_do_artista:
            artista = musica.artista.nome_artistico
            genero = musica.genero.genero
            self.__tela_musica.mostra_musica(0,
                {"nome_musica": musica.nome_musica, "artista": artista, "genero": genero})

    def pega_musica_artista(self, artista_escolhido):
        artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(
            artista_escolhido)
        # verifica se o artista existe
        if artista is None:
            self.__tela_musica.mostra_mnsg(
                "Não temos esse artista em nosso catalogo")

        # adiciona as musicas do artista em uma lista
        musicas_do_artista: List[Musica] = []
        for musica in self.__lista_musicas:
            if artista == musica.artista:
                musicas_do_artista.append(musica)
        # mensagem de erro para falta de musicas do artista
        if not musicas_do_artista:
            self.__tela_musica.mostra_mnsg("Não temos musicas desse Artista")

        return musicas_do_artista

    def verificar_musica(self, nome_musica, artista, genero):
        for musica in self.__lista_musicas:
            verificar_artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(
                artista)
            verificar_genero = self.__controlador_sistema.controlador_genero.seleciona_genero(
                genero)
            musica_verificar = Musica(nome_musica, verificar_artista, verificar_genero)
            if (musica.nome_musica == musica_verificar.nome_musica and
                musica.artista == musica_verificar.artista and musica.genero == musica_verificar.genero):
                return musica


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_musica, 2: self.listar_musicas,
                        3: self.listar_musicas_por_genero, 4: self.listar_musicas_por_artista, 5: self.retornar}

        while True:
            lista_opcoes[self.__tela_musica.tela_opcoes()]()
