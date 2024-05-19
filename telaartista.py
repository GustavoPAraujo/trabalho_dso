
class TelaArtista:

    def tela_opcoes(self):
        print("_____Artista_____")
        print("1: Cadastrar Artista")
        print("0: RETORNAR")

        while True:
            opcao = int(input("Escolha uma opção: "))

            if isinstance(opcao, int) and 0 <= opcao <= 4:
                return opcao
            else:
                print("Escolha uma opção valida")
    
    def criar_artista(self):
        print("_____Dados_do_Artista_____")
        nome = input("Digite o nome: ")
        nome_artistico = input("Digite o nome artistico: ")

        return {'nome': nome, "nome_artistico": nome_artistico  }
