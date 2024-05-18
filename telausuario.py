
class TelaUsuario:

    def tela_opcoes(self) -> int:
        print("--------Usuario--------")
        print("Escolha a opção:")
        print("1: Criar Usuario")
        print("2: Listar Usuarios")
        print("3: Adicionar Musicas Preferidas")
        print("4: Adicionar Amizade")
        print("5: Minhas amizades")
        print("0: Excluir Usuario")
        while True:

            opcao = int(input("Escolha uma opção: "))
            print("\n")

            if isinstance(opcao, int) and 0 <= opcao <= 10:
                return opcao
            else:
                print("Escolha uma opção valida")
                print("\n")

    def seleciona_usuario(self) -> str:
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

        amigo: str = input(print("Digite o nome de Usuario do Amigo: "))

        return amigo

    def musicas_preferidas(self) -> dict[str, str]:
        print("_____Digite_suas_3_músicas_favoritas_____")
        musica1 = input("Música 1: ")
        musica2 = input("Música 2: ")
        musica3 = input("Música 3: ")

        return {"Musica1": musica1, "Musica2": musica2, "Musica3": musica3}

    def mostra_mensagem(self, msg):
        print(msg)
