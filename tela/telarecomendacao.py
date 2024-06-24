import PySimpleGUI as sg

class TelaRecomendacao:
    def tela_opcoes(self):
        print('1: recomendacao por genero')
        print('2: recomendacao por artista')
        print('0: RETORNAR')
    
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if  0 <= opcao <= 2:
                    return opcao
                else:
                    print("\nEscolha uma opção válida\n")
            except ValueError:
                print("\nPor favor, insira um número inteiro.\n")






    def mostra_mnsg(self, mnsg):
        sg.popup(mnsg, title="Mensagem do Sistema")


    def close(self):
        if self.__window:
            self.__window.close()
            self.__window = None

    def open(self):
        button, values = self.__window.Read() #type: ignore
        return button, values
    
'''
    def pega_genero(self):
        print('__Insira o gênero__')
        genero = input('Gênero: ')
        return genero

    def pega_artista(self):
        print('__Insira o artista__')
        artista = input('Artista: ')
        return artista
'''