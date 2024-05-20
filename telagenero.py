
class TelaGenero:

    def tela_opcoes(self):
        print("_____Gênero_____")
        print("1: Cadastra Gênero")
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
    
    def criar_genero(self):
        print('_____Gênero_Músical_____')
        genero = input("Digite o nome Gênero: ")

        return {"genero": genero}

    def mostra_mnsg(self, mnsg):
        print(mnsg)