import PySimpleGUI as sg

class TelaArtista:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Artista')],
            [sg.Radio('Cadastrar Artista', "RADIO1", key='1')],
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


#fazer
'''
    def criar_artista(self):
        print("_____Dados_do_Artista_____")
        nome = input("Digite o nome: ")
        nome_artistico = input("Digite o nome artistico: ")

        return {'nome': nome, "nome_artistico": nome_artistico  }
    
    def mostra_mnsg(self, mnsg):
        print(mnsg)
'''