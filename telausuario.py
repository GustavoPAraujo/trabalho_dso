
class TelaUsuario:

    def tela_opcaoes(self):
        print("--------Usuario--------")
        print("Escolha a opção:")
        print("1: Criar Usuario")
        print("2: Listar Usuarios")
        print("3: Excluir Usuario")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def seleciona_usuario(self):
        usuario_selecionado = input("Insira o seu Nome de Usuario")
        return usuario_selecionado

    def pega_dados_usuario(self):
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
    
    def mostra_mensagem(self, msg):
        print(msg)
    