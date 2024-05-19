from controladorplaylist import ControladorPlaylist

class TelaPlaylist:
    def TelaOpcoes(self):
        print('___Tela Do Sistema___')
        print('1: Criar Playlist')
        print('2: Excluir Playlist')
        print('3: Selecionar Playlist')
        print('4: Alterar nome da Playlist')
        print('5: adicionar música')
        print('6: Excluir música')
        
        while True:
            opcao = int(input(print('Selecione sua Opção ')))
            if 0 < opcao < 7:
                return opcao
            else:
                return print(' OPÇÃO INVALIDA')
        
    def pegar_dados_Playlist(self) -> dict[str, str]:
        print("_____Insira_os_seus_dados_____")
        nome_playlist = input("Nome da Playlist")
        primeira_musica = input('Primeira Música')

        return {'Nome da Playlist': nome_playlist, 'Primeira Música': primeira_musica}
    
    def mostrar_playlist(self, nome_playlist):
        playlist = self.