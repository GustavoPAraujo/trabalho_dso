import PySimpleGUI as sg


class TelaUsuario:
    def __init__(self):
        self.__window = None
        self.init_components()

    def close(self):
        if self.__window:
            self.__window.close()
            self.__window = None

    def open(self):
        button, values = self.__window.Read() #type: ignore
        return button, values

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

    def init_components(self):
        sg.theme('DarkTeal4')
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
            [sg.Ok()]
        ]
        self.__window = sg.Window('Tela do Sistema', layout)

    def mostra_mensagem(self, mnsg):
        sg.popup(mnsg, title="Mensagem do Sistema")

    def seleciona_usuario(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Usuario')],
            [sg.Text('Insira o Nome de Usuario: ', size=(20,1)), sg.InputText('', key='nome_usuario')],
            [sg.Ok()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        nome_usuario = values['nome_usuario']

        self.close()
        return {"nome_usuario": nome_usuario}

    def pega_dados_usuario(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('Usuario')],
            [sg.Text('Insira o Nome do Usuario: ', size=(20,1)), sg.InputText('', key='nome')],
            [sg.Text('Insira o Nome de Usuario: ', size=(20,1)), sg.InputText('', key='nome_usuario')],
            [sg.Text('Insira o email do Usuario: ', size=(20,1)), sg.InputText('', key='email')],
            [sg.Text('Insira o telefone do Usuario: ', size=(20,1)), sg.InputText('', key='telefone')],
            [sg.Ok()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        nome = values['nome']
        nome_usuario = values['nome_usuario']
        email = values['email']
        telefone = values['telefone']

        self.close()
        return {"nome": nome, 'nome_usuario': nome_usuario, 'email': email, 'telefone': telefone}

    def mostrar_usuario(self, dados_ususario):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text(f"Nome do Usuario: {dados_ususario['nome']}")],
            [sg.Text(f"Nome de Usuario: {dados_ususario['nome_usuario']}")],
            [sg.Text(f"Email do Usuario: {dados_ususario['email']}")],
            [sg.Text(f"Telefone do Usuario: {dados_ususario['telefone']}")],
            [sg.Ok()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        self.close()

        
    def fazer_amizade(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("Digite o nome de Usuario do Amigo: ", size=(20,1)), sg.InputText('', key='amigo')],
            [sg.Ok()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        amigo = values['amigo']

        self.close()
        return {"amigo": amigo}

    def musicas_preferidas(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("_____Digite_suas_3_músicas_favoritas_____", size=(20,1))],
            [sg.Text("Música 1: ", size=(20,1)), sg.InputText('', key='Musica1')],
            [sg.Text("Música 1: ", size=(20,1)), sg.InputText('', key='Musica2')],
            [sg.Text("Música 1: ", size=(20,1)), sg.InputText('', key='Musica3')],
            [sg.Ok()]
        ]

        self.__window = sg.Window('Tela do Sistema', layout)

        button, values = self.open()
        musica1 = values['Musica1']
        musica2 = values['Musica2']
        musica3 = values['Musica3']

        self.close()
        return {"Musica1": musica1, "Musica2": musica2, "Musica3": musica3}
