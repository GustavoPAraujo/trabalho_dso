from tkinter import Button
import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):

        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Tela do Sistema')],
            [sg.Radio('cadastra_usuario ', "RADIO1", default=True)],
            [sg.Radio('cadastra_musica ', "RADIO1", default=True)],
            [sg.Radio('cadastra_artista ', "RADIO1", default=True)],
            [sg.Radio('cadastra_genero ', "RADIO1", default=True)],
            [sg.Radio('cadastra_playlist ', "RADIO1", default=True)],
            [sg.Radio('gera_recomendacao ', "RADIO1", default=True)],
            [sg.Radio('encerra_sistema ', "RADIO1", default=True)],
            [sg.Ok(), sg.Cancel()]
        ]
        self.__window = sg.Window('Tela do Sistema').Layout(layout)

    def tela_opcoes(self):
            self.init_components()
            button, values = self.__window.Read()
            opcao = 0
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            if values['3']:
                opcao = 3
            # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
            if values['0'] or button in (None,'Cancelar'):
                opcao = 0
            self.close()
            return opcao

    def close(self):
        self.__window.Close()
