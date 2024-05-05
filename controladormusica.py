from musica import Musica
from telamusica import TelaMusica


class ControladorMusica:
    def __init__(self) -> None:
        self.__lista_musicas = []
        self.__tela_musica = TelaMusica()

    def adicionar_musica(self, nome_musica, artista, genero):
        dados_musica = self.__tela_musica.pega_dados_musica()
        nova_musica = Musica( dados_musica["nome_musica"], dados_musica["artista"], dados_musica["genero"])
        if nova_musica not in self.__lista_musicas:
            self.__lista_musicas.append(nova_musica)
        
