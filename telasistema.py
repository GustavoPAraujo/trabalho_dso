
class TelaSistema:
    def tela_opcoes(self):
        print("_____tela_do_sistema_____")
        print("1: Usuario")
        print("2: Musicas")
        print("3: Artistas")
        print("4: Gêneros")
        print("5: PlayLists")
        print('6: Recomendações')


        while True:
            opcao = int(input("Escolha o opção: "))

            if isinstance(opcao, int) and 0 <= opcao <= 6:
                return opcao
            else:
                print("Escolha uma opção valida")