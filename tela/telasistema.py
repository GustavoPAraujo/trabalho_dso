from tkinter import Button
import PySimpleGUI as sg


class TelaSistema:
    def tela_opcoes(self):

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
        window = sg.Window('Tela do Sistema').Layout(layout)
        Button, values = window.Read()
        print(values[0], values[1], values[2], values[3], values[4], values[5], values[6])



'''
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if  0 <= opcao <= 6:
                    return opcao
                else:
                    print("\nEscolha uma opção válida\n")
            except ValueError:
                print("\nPor favor, insira um número inteiro.\n")
'''