from tabnanny import check
import PySimpleGUI as sg

class TelaGenero:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Gênero')],
            [sg.Radio('Cadastrar Gênero', "RADIO1", key='1')],
            [sg.Radio('Voltar', "RADIO1", key='2')],
            [sg.Ok(), sg.Cancel()]
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
    
    def criar_genero(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Gênero')],
            [sg.Text('Digite o nome do Gênero: ', size=(15,1)), sg.InputText('', key='genero')],
            [sg.Ok(), sg.Cancel()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        genero = values['genero']


        self.close()
        return {"genero" : genero}

    def open(self):
        button, values = self.__window.Read() #type: ignore
        return button, values
    

#fazer
'''
    def criar_genero(self):
        print('_____Gênero_Músical_____')
        genero = input("Digite o nome Gênero: ")

        return {"genero": genero}

    def mostra_mnsg(self, mnsg):
        print(mnsg)
'''