import PySimpleGUI as sg

class TelaMusica:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Tela do Sistema')],
            [sg.Radio('Adicionar uma Música', "RADIO1", key='1')],
            [sg.Radio('Listar Músicas', "RADIO1", key='2')],
            [sg.Radio('Listar Músicas por Gênero', "RADIO1", key='3')],
            [sg.Radio('Listar Músicas por Artista', "RADIO1", key='4')],
            [sg.Radio('Voltar', "RADIO1", key='5')],
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
    def pega_dados_musica(self):
        print("_____Insira_os_dados_da_musica_____")
        nome_musica = input("Nome da Musica: ")
        artista = input("Artista: ")
        genero = input("Gênero: ")

        return  {"nome_musica": nome_musica, "artista": artista, "genero": genero}

    def mostra_musica(self, dados_musica):
        print("Nome da Musica: ", dados_musica["nome_musica"])
        print("Nome do Artista: ", dados_musica["artista"])
        print("Gênero da Musica: ", dados_musica["genero"])
        print("\n")
    
    def selecionar_genero(self):
        print("_____Qual_Gênero_quero_ouvir_____")
        genero = input("Insira o Gênero: ")
        print("")
        return genero

    def seleciona_artista(self):
        print("_____Qual_Artista_\nquero_ouvir_____")
        artista = input("Insira o nome do Artista: ")
        print("\n")
        return artista

    def mostra_mnsg(self, mnsg):
        print(mnsg)
'''
