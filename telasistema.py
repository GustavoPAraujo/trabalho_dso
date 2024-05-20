
class TelaSistema:
    def tela_opcoes(self):
        print("_____tela_do_sistema_____")
        print("1: Usuario")
        print("2: Musicas")
        print("3: Artistas")
        print("4: Gêneros")
        print("5: PlayLists")
        print('6: Recomendações')
        print("0: Finalizar Sistema")


        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if  0 <= opcao <= 6:
                    return opcao
                else:
                    print("\nEscolha uma opção válida\n")
            except ValueError:
                print("\nPor favor, insira um número inteiro.\n")