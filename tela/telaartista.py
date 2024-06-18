
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
