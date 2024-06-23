import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Tela do Sistema')],
            [sg.Radio('Usuário', "RADIO1", key='1')],
            [sg.Radio('Música', "RADIO1", key='2')],
            [sg.Radio('Artista', "RADIO1", key='3')],
            [sg.Radio('Gênero', "RADIO1", key='4')],
            [sg.Radio('Playlist', "RADIO1", key='5')],
            [sg.Radio('Recomendação', "RADIO1", key='6')],
            [sg.Radio('Encerra sistema', "RADIO1", key='7')],
            [sg.Ok()]
        ]
        self.__window = sg.Window('Tela do Sistema', layout)

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

    def close(self):
        if self.__window:
            self.__window.close()
            self.__window = None
