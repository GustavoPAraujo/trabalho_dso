from playlist import PlayList
from telaplaylist import TelaPlaylist

class ControladorPlaylist:
    def __init__(self) -> None:
        self.__lista_playlist = [PlayList]
        self.__tela_playlist = TelaPlaylist()
    
    def criar_playlist(self):
        playlist = self.__tela_playlist.pegar_dados_Playlist()
        playlist_nova = PlayList(playlist['Nome da Playlist'], playlist['Primeira Música'])
        for playlist in self.__lista_playlist:
            if playlist not in self.__lista_playlist:
                self.__lista_playlist.append(playlist)
    
    def chamar_add_musica(self):
        return PlayList.adicionar_musica_playlist()

    def chamar_remove_musica(self):
        return PlayList.excluir_musica()
    
    def selecionar_playlist(self, nome_playlist):
        for playlist in self.__lista_playlist:
            if nome_playlist == playlist.nome_playlist:
                return playlist
    
    def mostra_playlist(self):
        playlist = 


       
    
   
    ### def abre_tela(self):
        lista_opcoes = {1: self.chamar_add_musica, 2: self.chamar_remove_musica, 3: self.selecionar_playlist,
                        4: self.m, 0: self.excuir_usuario}

        while True:
            lista_opcoes[self.__tela_playlist.TelaOpcoes()]()
