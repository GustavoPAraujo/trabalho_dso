from typing import List
from musica import Musica
from telamusica import TelaMusica
from controladorsistema import ControladorSistema

class ControladorMusica:
    def __init__(self, controlador_sistema: ControladorSistema) -> None:
        self.__lista_musicas: List[Musica] = list()
        self.__tela_musica = TelaMusica()
        self.__controlador_sistema: ControladorSistema = controlador_sistema

    def adicionar_musica(self):
        dados_musica = self.__tela_musica.pega_dados_musica()
        artista = self.__controlador_sistema.__controlador_artista.pega_artista_por_nome(dados_musica["artista"])
        genero = self.__controlador_sistema.__controlador_genero.seleciona_genero(dados_musica["genero"])

        nova_musica = Musica(
            dados_musica["nome_musica"], artista, genero) # type: ignore
        
        if nova_musica.artista is None:
            self.__tela_musica.mostra_mnsg("Esse artista não existe!")
            return
        elif nova_musica.genero is None:
            self.__tela_musica.mostra_mnsg("Esse gênero não existe!")
            return
        elif nova_musica not in self.__lista_musicas:
            self.__lista_musicas.append(nova_musica)

    def listar_musicas(self):
        for musica in self.__lista_musicas:
            self.__tela_musica.mostra_musica(
                {"nome_musica": musica.nome_musica, "artista": musica.artista, "genero": musica.genero})


# arrumar as listagens por genero e artista
    def listar_musicas_por_genero(self):
        genero = self.__tela_musica.selecionar_genero()
        for musica in self.__lista_musicas:
            if genero == musica.genero:
                self.__tela_musica.mostra_musica(genero)

    def listar_musicas_por_artista(self):
        artista = self.__tela_musica.seleciona_artista()
        for musica in self.__lista_musicas:
            if artista == musica.artista:
                self.__tela_musica.mostra_musica(artista)
        
    def adiciona_musica_na_playlist(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_musica, 2: self.listar_musicas,
                        3: self.listar_musicas_por_genero, 4: self.listar_musicas_por_artista, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_musica.tela_opcoes()]()
