from typing import List
from playlist import PlayList
from telaplaylist import TelaPlaylist

class ControladorPlaylist:
    def __init__(self, controlador_sistema) -> None:
        self.__lista_playlist: List[PlayList] = list()
        self.__tela_playlist = TelaPlaylist()
        self.__controlador_sistema = controlador_sistema
    #1
    def criar_playlist(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()
        dados_primeira_musica = self.__tela_playlist.pegar_musica()
        nome_musica = dados_primeira_musica['nome_musica']
        artista = dados_primeira_musica['artista']
        genero = dados_primeira_musica['genero']
        musica_verificada = self.__controlador_sistema.controlador_musica.verificar_musica(nome_musica,artista,genero)
        nova_playlist = PlayList(nome_playlist, musica_verificada)
        self.__lista_playlist.append(nova_playlist)
        print(PlayList.musicas_playlist)
        print('PlayList criada com sucesso')
    
    #2
    def excluir_playlist(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()
        for playlist in self.__lista_playlist:
            if nome_playlist == playlist.nome_playlist:
                self.__lista_playlist.remove(playlist)
            else:
                print('PlayList não existente')

    #3
    def selecionar_playlist(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()
        for playlist in self.__lista_playlist:
            if nome_playlist == playlist.nome_playlist:
                return {'nome_playlist': nome_playlist, 'musicas': playlist.musicas_playlist} 
            else:
                print('PlayList não existente')

    #4
    #fazer
    def alterar_nome_playlist(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()
        for playlist in self.__lista_playlist:
            if nome_playlist == playlist.nome_playlist:
                novo_nome = self.__tela_playlist.alterar_nome_playlist()
                return novo_nome
            else:
                print( 'Essa PlayList não existe')

    #5
    def adicionar_musica(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()
        for playlist in self.__lista_playlist:
            if nome_playlist == playlist.nome_playlist:
                dados_musica = self.__tela_playlist.pegar_musica()
                nome_musica = dados_musica['nome_musica']
                artista = dados_musica['artista']
                genero = dados_musica['genero']
                musica_verificada = self.__controlador_sistema.controlador_musica.verificar_musica(nome_musica,artista,genero)
                if musica_verificada is not None and musica_verificada not in playlist:
                    playlist.musicas_playlist.append(musica_verificada)
                    return musica_verificada
                else:
                    print('Essa música não existe')
            else:
                print( 'Essa playlist não existe')

                

    #6
    #fazer
    def excluir_musica(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()
        for playlist in self.__lista_playlist:
            if nome_playlist == playlist.nome_playlist:
                dados_musica = self.__tela_playlist.pegar_musica()
                nome_musica = dados_musica['nome_musica']
                artista = dados_musica['artista']
                genero = dados_musica['genero']
                musica_verificada = self.__controlador_sistema.controlador_musica.verificar_musica(nome_musica,artista,genero)
                if musica_verificada is not None and musica_verificada in playlist:
                    playlist.musicas_playlist.remove(musica_verificada)
                    return musica_verificada
                else:
                    print('música não presente na PlayList')
            else:
                print( 'Essa PlayList não existe' )


    def retornar(self):
        self.__controlador_sistema.abre_tela()
   
    def abre_tela(self):
        lista_opcoes = {1: self.criar_playlist, 2: self.excluir_playlist, 3: self.selecionar_playlist,
                        4: self.alterar_nome_playlist, 5: self.adicionar_musica, 6: self.excluir_musica, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_playlist.tela_opcoes()]()
