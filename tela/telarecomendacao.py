import PySimpleGUI as sg

class TelaRecomendacao:
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
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Recomendações')],
            [sg.Radio('Recomendação por genero', "RADIO1", key='1')],
            [sg.Radio('Recomendação por artista', "RADIO2", key='2')],
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
    
    def pega_genero(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Recomendações por Genero')],
            [sg.Text('Digite o nome do Gênero: ', size=(20,1)), sg.InputText('', key='genero')],
            [sg.Ok()]
        ]
        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        genero = values['genero']

        self.close()
        return {"genero" : genero}
    
    def pega_artista(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Recomendações por Artista')],
            [sg.Text('Digite o nome do artista: ', size=(20,1)), sg.InputText('', key='artista')],
            [sg.Ok()]
        ]
        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        artista = values['artista']

        self.close()
        return {"artista" : artista}
