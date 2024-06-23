import PySimpleGUI as sg

class TelaArtista:
    def __init__(self):
        self.__window = None
        self.init_components()

    def open(self):
        button, values = self.__window.Read() #type: ignore
        return button, values

    def close(self):
        if self.__window:
            self.__window.close()
            self.__window = None

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
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Artista')],
            [sg.Radio('Cadastrar Artista', "RADIO1", key='1')],
            [sg.Radio('Voltar', "RADIO1", key='2')],
            [sg.Ok()]
        ]
        self.__window = sg.Window('Tela do Sistema', layout)

    def criar_artista(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Artista')],
            [sg.Text('Digite o nome do Artista: ', size=(20,1)), sg.InputText('', key='nome')],
            [sg.Text('Digite o nome Artistico: ', size=(20,1)), sg.InputText('', key='nome_artistico')],
            [sg.Ok()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        nome = values['nome']
        nome_artistico = values['nome_artistico']


        self.close()
        return {"nome" : nome, "nome_artistico" : nome_artistico}

    def mostra_mnsg(self, mnsg):
        sg.popup(mnsg, title="Mensagem do Sistema")