

class TelaPlaylist:
    def tela_opcoes(self):
        print('___Tela Do Sistema___')
        print('1: Criar Playlist')
        print('2: Excluir Playlist')
        print('3: Selecionar Playlist')
        print('4: Alterar nome da Playlist')
        print('5: adicionar música')
        print('6: Excluir música')
        print("0: RETORNAR")
        
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if  0 <= opcao <= 6:
                    return opcao
                else:
                    print("\nEscolha uma opção válida\n")
            except ValueError:
                print("\nPor favor, insira um número inteiro.\n")
        
    def pega_nome_playlist(self):
        print("_____Escolha nome da Playlist_____")
        nome_playlist = input("Nome da Playlist ")
        return nome_playlist
    
    def alterar_nome_playlist(self):
        print('__Escolha novo nome da PlayList___')
        novo_nome = input('Novo nome da Playlist ')
        return novo_nome

    def pegar_musica(self):
        print('___Digite_informações_da_música___')
        nome_musica = input('Música: ')
        artista = input('Artista: ')
        genero = input('Gênero: ')

        return {'nome_musica': nome_musica, 'artista': artista, 'genero': genero}

    def mostrar_playlist(self, dados_playlist):
        nome = dados_playlist['nome_playlist']
        print(nome)
        musicas = dados_playlist['musicas']
        for musica in musicas:
            print(musica)