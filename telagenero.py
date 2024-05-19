
class TelaGenero:

    def tela_opcoes(self):
        print("_____Gênero_____")

        opcao = int(input("Escolha uma opção: "))

        return opcao
    
    def criar_genero(self):
        print('_____Gênero_Músical_____')
        genero = input(print("Digite o nome Gênero: "))

        return {"genero": genero}
