import PySimpleGUI as sg

class TelaPlaylist:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.read() # type: ignore
        opcao = 0

        if values:
            for key in values:
                if values[key]:
                    opcao = int(key)

        if button in (None, 'Cancel'):
            opcao = 0
        
        self.close()
        return opcao

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Tela do Sistema')],
            [sg.Radio('Criar Playlist', "RADIO1", key='1')],
            [sg.Radio('Excluir Playlist', "RADIO1", key='2')],
            [sg.Radio('Selecionar Playlist', "RADIO1", key='3')],
            [sg.Radio('Alterar nome da Playlist', "RADIO1", key='4')],
            [sg.Radio('adicionar música', "RADIO1", key='5')],
            [sg.Radio('Excluir música', "RADIO1", key='6')],
            [sg.Radio('Voltar', "RADIO1", key='7')],
            [sg.Ok(), sg.Cancel()]
        ]
        self.__window = sg.Window('Tela do Sistema', layout)
    
    def mostra_mnsg(self, mnsg):
        sg.popup(mnsg, title="Mensagem do Sistema")


    def close(self):
        if self.__window:
            self.__window.close()
            self.__window = None

    def open(self):
        button, values = self.__window.Read() #type: ignore
        return button, values

    def pega_nome_playlist(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('_____Escolha nome da Playlist_____')],
            [sg.Text('Nome da Playlist : ', size=(20,1)), sg.InputText('', key='nome_playlist')],
            [sg.Ok(), sg.Cancel()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        nome_playlist = values['nome_playlist']

        return nome_playlist

    def alterar_nome_playlist(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('__Escolha novo nome da PlayList___')],
            [sg.Text('Novo nome da Playlist: ', size=(20,1)), sg.InputText('', key='novo_nome')],
            [sg.Ok(), sg.Cancel()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        novo_nome = values['novo_nome']

        return novo_nome
    
    def pegar_musica(self):
        

#fazer
''' 
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
        print(musicas)
'''