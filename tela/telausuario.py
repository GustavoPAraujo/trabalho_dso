import PySimpleGUI as sg

class TelaUsuario:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Tela do Sistema')],
            [sg.Radio('Criar Usuário', "RADIO1", key='1')],
            [sg.Radio('Excluir Usuário', "RADIO1", key='2')],
            [sg.Radio('Listar Usuários', "RADIO1", key='3')],
            [sg.Radio('Adicionar músicas preferidas', "RADIO1", key='4')],
            [sg.Radio('Adicionar Amizades', "RADIO1", key='5')],
            [sg.Radio('Minhas amizades', "RADIO1", key='6')],
            [sg.Radio('Musicas preferidas dos meus amigos', "RADIO1", key='7')],
            [sg.Radio('Voltar', "RADIO1", key='8')],
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
    def seleciona_usuario(self) -> str:
        self.mostra_mensagem("")
        usuario_selecionado = input("Insira o Nome de Usuario: ")
        return usuario_selecionado

    def pega_dados_usuario(self) -> dict[str, str]:
        print("_____Insira_os_seus_dados_____")
        nome = input("Nome: ")
        nome_usuario = input("Nome de Usuario: ")
        email = input("Email: ")
        telefone = input("Telefone: ")

        return {"nome": nome, "nome_usuario": nome_usuario, "email": email, "telefone": telefone}

    def mostrar_usuario(self, dados_usuario):
        print("Nome do Usuario: ", dados_usuario["nome"])
        print("Nome de Usuario: ", dados_usuario["nome_usuario"])
        print("Email do Usuario: ", dados_usuario["email"])
        print("Telefone do Usuario: ", dados_usuario["telefone"])
        print("\n")

    def fazer_amizade(self) -> str:
        self.mostra_mensagem("")
        amigo: str = input("Digite o nome de Usuario do Amigo: ")
        return amigo

    def musicas_preferidas(self) -> dict[str, str]:
        print("_____Digite_suas_3_músicas_favoritas_____")
        musica1 = input("Música 1: ")
        musica2 = input("Música 2: ")
        musica3 = input("Música 3: ")

        return {"Musica1": musica1, "Musica2": musica2, "Musica3": musica3}

    def mostra_mensagem(self, msg):
        print(msg)
'''