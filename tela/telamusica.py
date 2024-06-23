import PySimpleGUI as sg

class TelaMusica:
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
            [sg.Radio('Adicionar uma Música', "RADIO1", key='1')],
            [sg.Radio('Listar Músicas', "RADIO1", key='2')],
            [sg.Radio('Listar Músicas por Gênero', "RADIO1", key='3')],
            [sg.Radio('Listar Músicas por Artista', "RADIO1", key='4')],
            [sg.Radio('Voltar', "RADIO1", key='5')],
            [sg.Ok()]
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

    def pega_dados_musica(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Insira os dados da Musica')],
            [sg.Text('Digite o nome da Musica: ', size=(20,1)), sg.InputText('', key='nume_musica')],
            [sg.Text('Digite o nome do Artista: ', size=(20,1)), sg.InputText('', key='artista')],
            [sg.Text('Digite o nome do Genero: ', size=(20,1)), sg.InputText('', key='genero')],
            [sg.Ok()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        nume_musica = values['nume_musica']
        artista = values['artista']
        genero = values['genero']


        self.close()
        return {'nume_musica': nume_musica ,'artista': artista,"genero" : genero}
    
    def selecionar_genero(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Insira o Genero')],
            [sg.Text('Digite o Genero: ', size=(20,1)), sg.InputText('', key='genero')],
            [sg.Ok()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        genero = values['genero']

        return genero

    def seleciona_artista(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Insira o nome do artista')],
            [sg.Text('Digite nome do artista ', size=(20,1)), sg.InputText('', key='artista')],
            [sg.Ok()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        artista = values['artista']

        return artista

    def mostra_musica(self, dados_musica):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text(f"Nome da Musica: {dados_musica['nome_musica']}")],
            [sg.Text(f"Nome do Artista: {dados_musica['artista']}")],
            [sg.Text(f"Gênero da Musica: {dados_musica['genero']}")],
            [sg.Ok()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)