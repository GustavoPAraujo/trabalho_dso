
class TelaMusica:
    
    def tela_opcoes(self):
        print("1: Adicionar uma Música")
        print("2: Listar Músicas")

    
    def pega_dados_musica(self):
        print("_____Insira_os_dad0s_da_musica_____")
        nome_musica = input("Nome da Musica: ")
        artista = input("Artista: ")
        genero = input("Gênero: ")

        return  {"nome_musica": nome_musica, "artista": artista, "genero": genero}

    def mostra_musica(self, dados_musica):
        print("Nome da Musica: ", dados_musica["nome_musica"])
        print("Nome do Artista: ", dados_musica["artista"])
        print("Gênero da Musica: ", dados_musica["genero"])
        print("\n")