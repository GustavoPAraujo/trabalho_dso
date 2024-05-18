
class TelaSistema:
    def tela_opcoes(self):
        print("_____tela_do_sistema_____")
        print("1: Usuario")
        print("2: Musicas")


        while True:
            opcao = int(input(print("Escolha uma opção: ")))

            if isinstance(opcao, int) and 0 <= opcao < 4:
                return opcao
            else:
                print("Escolha uma opção valida")