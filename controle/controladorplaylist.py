from typing import List
from entidades.playlist import PlayList
from tela.telaplaylist import TelaPlaylist
from DAOs.playlist_dao import PlaylistDAO

class ControladorPlaylist:
    def __init__(self, controlador_sistema) -> None:
        self.__tela_playlist = TelaPlaylist()
        self.__controlador_sistema = controlador_sistema
        self.__playlist_dao = PlaylistDAO()

    #1
    def criar_playlist(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()

        # Verifica se a playlist já existe
        playlist = self.__playlist_dao.get(nome_playlist)
        if playlist is not None:
            self.__tela_playlist.mostra_mnsg('já existe uma Playlist com esse nome')
            return

        # Obtém os dados da primeira música
        dados_primeira_musica = self.__tela_playlist.pegar_musica()
        nome_musica = dados_primeira_musica['nome_musica']
        artista = dados_primeira_musica['artista']
        genero = dados_primeira_musica['genero']

        # Verifica a existência da música
        musica_verificada = self.__controlador_sistema.controlador_musica.verificar_musica(nome_musica, artista, genero)
        
        if musica_verificada is None:
            print('A música não foi encontrada ou não pôde ser verificada.')
            return
        
        # Cria a nova playlist e adiciona a música verificada
        nova_playlist = PlayList(nome_playlist, musica_verificada)
        self.__playlist_dao.add(nova_playlist.nome_playlist, nova_playlist)

        self.__tela_playlist.mostra_mnsg('Playlist criada com sucesso')

    #2
    def excluir_playlist(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()

        #verificar se a playlist já existe
        playlist = self.__playlist_dao.get(nome_playlist)
        if playlist is None:
            self.__tela_playlist.mostra_mnsg('Playlist inexistente')
            return
        
        #excluir playlist
        playlist_excluida = self.__playlist_dao.remove(nome_playlist)
        self.__tela_playlist.mostra_mnsg('Playlist excluida com sucesso')
        
    #3
    def selecionar_playlist(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()
        playlist = self.__playlist_dao.get(nome_playlist)
        if playlist is not None:
            dado_playlist = {'nome_playlist': nome_playlist, 'musicas': playlist.musicas_playlist} 
            self.__tela_playlist.mostrar_playlist(dado_playlist)
        else:
            self.__tela_playlist.mostra_mnsg('Playlist inexistente')
    #4
    #fazer
    def alterar_nome_playlist(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()
        for playlist in self.__lista_playlist:
            if nome_playlist == playlist.nome_playlist:
                novo_nome = self.__tela_playlist.alterar_nome_playlist()
                playlist.nome_playlist = novo_nome
                print('Nome editado com sucesso')
            else:
                print( 'Essa PlayList não existe')

    #5
    def adicionar_musica(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()

        playlist_encontrada = None
        for playlist in self.__lista_playlist:
            if nome_playlist == playlist.nome_playlist:
                playlist_encontrada = playlist
                return playlist_encontrada
            else:
                print('Essa playlist não existe')
                return
            
        dados_musica = self.__tela_playlist.pegar_musica()
        nome_musica = dados_musica['nome_musica']
        artista = dados_musica['artista']
        genero = dados_musica['genero']
        musica_verificada = self.__controlador_sistema.controlador_musica.verificar_musica(nome_musica, artista, genero)

        if musica_verificada not in playlist_encontrada.musicas:
            playlist_encontrada.musicas.append(musica_verificada)
            print('Música adicionada com sucesso')
        else:
            print('Música já presente na playlist')
        

    #6
    #fazer
    def excluir_musica(self):
        nome_playlist = self.__tela_playlist.pega_nome_playlist()

        playlist_encontrada = None
        for playlist in self.__lista_playlist:
            if nome_playlist == playlist.nome_playlist:
                playlist_encontrada = playlist
                return playlist_encontrada
            else:
                print('Essa playlist não existe')
                return
            
        dados_musica = self.__tela_playlist.pegar_musica()
        nome_musica = dados_musica['nome_musica']
        artista = dados_musica['artista']
        genero = dados_musica['genero']
        musica_verificada = self.__controlador_sistema.controlador_musica.verificar_musica(nome_musica, artista, genero)

        if musica_verificada not in playlist_encontrada.musicas:
            playlist_encontrada.musicas.remove(musica_verificada)
            print('Música removida com sucesso')
        else:
            print('Música não presente na playlist')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_playlist, 2: self.excluir_playlist, 3: self.selecionar_playlist,
                        4: self.alterar_nome_playlist, 5: self.adicionar_musica, 6: self.excluir_musica, 7: self.retornar}

        while True:
            lista_opcoes[self.__tela_playlist.tela_opcoes()]()
