
class TelaGenero:

    def tela_opcoes(self):
        print("_____Gênero_____")
        print("1: Cadastra Gênero")
        print("0: RETORNAR")

        while True:
            opcao = int(input("Escolha uma opção: "))

            if isinstance(opcao, int) and 0 <= opcao <= 4:
                return opcao
            else:
                print("Escolha uma opção valida")
    
    def criar_genero(self):
        print('_____Gênero_Músical_____')
        genero = input(print("Digite o nome Gênero: "))

        return {"genero": genero}
