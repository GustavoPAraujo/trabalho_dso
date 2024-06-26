from entidades.artista import Artista
from entidades.musica import Musica
from tela.telamusica import TelaMusica
from DAOs.musica_dao import MusicaDAO


class ControladorMusica:
    def __init__(self, controlador_sistema):
        self.__tela_musica = TelaMusica()
        self.__controlador_sistema = controlador_sistema
        self.__musica_dao = MusicaDAO()

    def adicionar_musica(self):
        dados_musica = self.__tela_musica.pega_dados_musica()

        artista: Artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(
            dados_musica["artista"])
        if artista is None:
            self.__tela_musica.mostra_mnsg("Artista não encontrado.")
            return
        
        genero = self.__controlador_sistema.controlador_genero.seleciona_genero(
            dados_musica["genero"])
        if genero is None:
            self.__tela_musica.mostra_mnsg("Gênero não encontrado.")
            return

        musica_existente = self.verificar_musica(
            dados_musica["nome_musica"], artista, genero)

        if musica_existente is not None:
            self.__tela_musica.mostra_mnsg("Essa música já está cadastrada.")
            return

        nova_musica = Musica(
            dados_musica["nome_musica"], artista, genero)

        # Adiciona a música ao DAO
        self.__musica_dao.add(dados_musica["nome_musica"], nova_musica)

        self.__tela_musica.mostra_mnsg("Música criada com sucesso!")


    def listar_musicas(self):
        musicas = self.__musica_dao.get_all()

        if not musicas:
            self.__tela_musica.mostra_mnsg("Não há músicas cadastradas.")
            return
        
        n_musica = 1
        for musica in musicas:
            artista = musica.artista.nome_artistico
            genero = musica.genero.genero

            dados_musica = {"nome_musica": musica.nome_musica, "artista": artista, "genero": genero}
            self.__tela_musica.mostra_musica(n_musica, dados_musica)
            n_musica += 1

    def listar_musicas_por_genero(self):
        pega_genero = self.__tela_musica.selecionar_genero()
        genero = self.__controlador_sistema.controlador_genero.seleciona_genero(
            pega_genero)

        if genero is None:
            self.__tela_musica.mostra_mnsg("Não há músicas com esse Gênero.")
            return

        musicas_do_genero = self.__musica_dao.get_by_genero(genero)

        if not musicas_do_genero:
            self.__tela_musica.mostra_mnsg("Não há músicas com esse Gênero.")
            return

        n_musica = 1
        for musica in musicas_do_genero:
            artista = musica.artista.nome_artistico
            genero = musica.genero.genero
            self.__tela_musica.mostra_musica(n_musica,
                {"nome_musica": musica.nome_musica, "artista": artista, "genero": genero})
            n_musica += 1

    def pega_musica_genero(self, genero_escolhido):
        genero = self.__controlador_sistema.controlador_genero.seleciona_genero(genero_escolhido)
        # verifica se o genero existe
        if genero is None:
            self.__tela_musica.mostra_mnsg("Não temos musicas com esse Gênero")
   
            return
        # adiciona as musicas do genero em uma lista
        musicas_do_genero: List[Musica] = []
        for musica in self.__lista_musicas:
            if genero == musica.genero:
                musicas_do_genero.append(musica)
        # mensagem de erro para falta de musicas do genero
        if not musicas_do_genero:
            self.__tela_musica.mostra_mnsg("Não temos musicas com esse Gênero")

        return musicas_do_genero

    def listar_musicas_por_artista(self):
        pega_artista = self.__tela_musica.seleciona_artista()
        artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(
            pega_artista)

        if artista is None:
            self.__tela_musica.mostra_mnsg("Não há músicas desse Artista.")
            return

        musicas_do_artista = self.__musica_dao.get_by_artista(artista)

        if not musicas_do_artista:
            self.__tela_musica.mostra_mnsg("Não há músicas desse Artista.")
            return

        n_musica = 1
        self.__tela_musica.mostra_mnsg(f"Músicas de: {artista}")
        for musica in musicas_do_artista:
            artista = musica.artista.nome_artistico
            genero = musica.genero.genero
            self.__tela_musica.mostra_musica(n_musica,
                {"nome_musica": musica.nome_musica, "artista": artista, "genero": genero})
            n_musica += 1

    def pega_musica_artista(self, artista_escolhido):
        artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(
            artista_escolhido)
        # verifica se o artista existe
        if artista is None:
            self.__tela_musica.mostra_mnsg(
                "Não temos esse artista em nosso catalogo")

        # adiciona as musicas do artista em uma lista
        musicas_do_artista: List[Musica] = []
        for musica in self.__lista_musicas:
            if artista == musica.artista:
                musicas_do_artista.append(musica)
        # mensagem de erro para falta de musicas do artista
        if not musicas_do_artista:
            self.__tela_musica.mostra_mnsg("Não temos musicas desse Artista")

        return musicas_do_artista

    def verificar_musica(self, nome_musica, artista, genero):
        musica_existente = self.__musica_dao.get_by_details(nome_musica, artista, genero)
        return musica_existente


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_musica, 2: self.listar_musicas,
                        3: self.listar_musicas_por_genero, 4: self.listar_musicas_por_artista, 5: self.retornar}

        while True:
            lista_opcoes[self.__tela_musica.tela_opcoes()]()
