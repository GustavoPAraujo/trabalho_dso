

import PySimpleGUI as sg
class TelaSistema:
    def tela_opcoes(self):
        layout = [
            [sg.Text('Tela do Sistema')],
            [sg.Radio('cadastra_usuario ', "RADIO1", default=True)],
            [sg.Radio('cadastra_musica ', "RADIO1", default=True)],
            [sg.Radio('cadastra_artista ', "RADIO1", default=True)],
            [sg.Radio('cadastra_genero ', "RADIO1", default=True)],
            [sg.Radio('cadastra_playlist ', "RADIO1", default=True)],
            [sg.Radio('gera_recomendacao ', "RADIO1", default=True)],
            [sg.Radio('encerra_sistema ', "RADIO1", default=True)],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Simple data entry window').Layout(layout)
        button, values = window.Read()
        print(button, values[0], values[1], values[2])


        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if  0 <= opcao <= 6:
                    return opcao
                else:
                    print("\nEscolha uma opção válida\n")
            except ValueError:
                print("\nPor favor, insira um número inteiro.\n")