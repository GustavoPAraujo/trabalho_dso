
class TelaArtista:

    def tela_opcoes(self):
        print("_____Artista_____")
        print("1: Cadastrar Artista")

        opcao = int(input())
        return opcao
    
    def criar_artista(self):
        print("_____Dados_do_Artista_____")
        nome = input(print("Digite o nome: "))
        nome_artistico = input(print("Digite o nome artistico: "))

        return {'nome': nome, "nome_artistico": nome_artistico}
