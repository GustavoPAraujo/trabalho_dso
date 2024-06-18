import PySimpleGUI as sg

class TelaArtista:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Artista')],
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

'''
class TelaArtista:

    def tela_opcoes(self):
        print("_____Artista_____")
        print("1: Cadastrar Artista")
        print("0: RETORNAR")
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if  0 <= opcao <= 1:
                    return opcao
                else:
                    print("\nEscolha uma opção válida\n")
            except ValueError:
                print("\nPor favor, insira um número inteiro.\n")
    
    def criar_artista(self):
        print("_____Dados_do_Artista_____")
        nome = input("Digite o nome: ")
        nome_artistico = input("Digite o nome artistico: ")

        return {'nome': nome, "nome_artistico": nome_artistico  }
    
    def mostra_mnsg(self, mnsg):
        print(mnsg)
'''