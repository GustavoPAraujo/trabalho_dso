class TelaPlaylist:
    def TelaOpcoes(self):
        print('___Tela Do Sistema___')
        print('1: Incluir Música')
        print('2: Excluir música')
        print('3: Selecionar Playlist')
        print('4: Alterar nome da Playlist')
        print('5: Adicionar Playlist')
        print('6: Excluir Playlist')
        
        while True:
            opcao = int(input(print('Selecione sua Opção ')))
            if 0 < opcao < 7:
                return opcao
            else:
                return print(' OPÇÃO INVALIDA')
        
        