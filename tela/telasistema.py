import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Tela do Sistema')],
            [sg.Radio('cadastra_usuario', "RADIO1", key='1')],
            [sg.Radio('cadastra_musica', "RADIO1", key='2')],
            [sg.Radio('cadastra_artista', "RADIO1", key='3')],
            [sg.Radio('cadastra_genero', "RADIO1", key='4')],
            [sg.Radio('cadastra_playlist', "RADIO1", key='5')],
            [sg.Radio('gera_recomendacao', "RADIO1", key='6')],
            [sg.Radio('encerra_sistema', "RADIO1", key='7')],
            [sg.Ok(), sg.Cancel()]
        ]
        self.__window = sg.Window('Tela do Sistema', layout)

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.read()
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