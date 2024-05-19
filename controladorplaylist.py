from playlist import PlayList
from telaplaylist import TelaPlaylist

class ControladorPlaylist:
    def __init__(self, controlador_sistema) -> None:
        self.__lista_playlist = [PlayList]
        self.__tela_playlist = TelaPlaylist()
        self.__controlador_sistema = controlador_sistema
    
    def criar_playlist(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()
        dados_primeira_musica = self.__tela_playlist.pegar_musica()
        nome_musica = dados_primeira_musica['nome_musica']
        artista = dados_primeira_musica['artista']
        genero = dados_primeira_musica['genero']
        musica_verificada = self.__controlador_sistema.controlador_musica.verificar_musica(nome_musica,artista,genero)
        if musica_verificada is not None:
            
        playlist_nova = PlayList(playlist['Nome da Playlist'], playlist['Primeira Música'])
        for playlist in self.__lista_playlist:
            if playlist not in self.__lista_playlist:
                self.__lista_playlist.append(playlist)
    
    def adicionar_musica(self):
        dados_musica = self.__tela_playlist.pegar_musica()
        nome_musica = dados_musica['nome_musica']
        artista = dados_musica['artista']
        genero = dados_musica['genero']
        musica_verificada = self.__controlador_sistema.controlador_musica.verificar_musica(nome_musica,artista,genero)
        if musica_verificada is not None:



    
    def selecionar_playlist(self, nome_playlist):
        for playlist in self.__lista_playlist:
            if nome_playlist == playlist.nome_playlist:
                return playlist
    
    
       
    
   
    ### def abre_tela(self):
        lista_opcoes = {1: self.chamar_add_musica, 2: self.chamar_remove_musica, 3: self.selecionar_playlist,
                        4: self.m, 0: self.excuir_usuario}

        while True:
            lista_opcoes[self.__tela_playlist.TelaOpcoes()]()
