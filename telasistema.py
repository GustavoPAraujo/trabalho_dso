

import PySimpleGUI as sg
class TelaSistema:
    def tela_opcoes(self):

        layout = [
            [sg.Text('Please enter your Name, Address, Phone')],
            [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
            [sg.Text('Address', size=(15, 1)), sg.InputText('address')],
            [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Simple data entry window').Layout(layout)
        button, values = window.Read()
        print(button, values[0], values[1], values[2])

