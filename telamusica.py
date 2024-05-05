
class TelaMusica:
    
    def tela_opcoes(self):
        print("")

    
    def pega_dados_musica(self):
        print("_____Insira_os_dad0s_da_musica_____")
        nome_musica = input("Nome da Musica: ")
        artista = input("Artista: ")
        genero = input("Gênero: ")

        return  {"nome_musica": nome_musica, "artista": artista, "genero": genero}