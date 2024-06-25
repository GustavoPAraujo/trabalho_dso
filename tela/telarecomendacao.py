import PySimpleGUI as sg

class TelaRecomendacao:
    def __init__(self):
        self.__window = None
        self.init_components()
    
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if  0 <= opcao <= 2:
                    return opcao
                else:
                    print("\nEscolha uma opção válida\n")
            except ValueError:
                print("\nPor favor, insira um número inteiro.\n")

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
            [sg.Text('Recomendações')],
            [sg.Text('Digite o nome do Gênero: ', size=(20,1)), sg.InputText('', key='genero')],
            [sg.Ok()]
        ]
        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        genero = values['genero']

        self.close()
        return {"genero" : genero}
    

'''
    def pega_genero(self):
        print('__Insira o gênero__')
        genero = input('Gênero: ')
        return genero

    def pega_artista(self):
        print('__Insira o artista__')
        artista = input('Artista: ')
        return artista
'''