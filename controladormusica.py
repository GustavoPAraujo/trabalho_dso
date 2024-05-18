from musica import Musica
from telamusica import TelaMusica


class ControladorMusica:
    def __init__(self) -> None:
        self.__lista_musicas = []
        self.__tela_musica = TelaMusica()

    def adicionar_musica(self):
        dados_musica = self.__tela_musica.pega_dados_musica()
        nova_musica = Musica( dados_musica["nome_musica"], dados_musica["artista"], dados_musica["genero"])
        if nova_musica not in self.__lista_musicas:
            self.__lista_musicas.append(nova_musica)
        
    def listar_musicas(self):
        for musica in self.__lista_musicas:
            self.__tela_musica.mostra_musica({"nome_musica": musica.nome_musica, "artista": musica.artista, "genero": musica.genero})
    


    # IMPORTANTE 
    # Fazer a tela
    def abre_tela(self):
        pass
    
    