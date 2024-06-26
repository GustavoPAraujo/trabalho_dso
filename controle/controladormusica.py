from entidades.artista import Artista
from entidades.genero import Genero
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

        artista: Artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(dados_musica["artista"])
        if artista is None:
            self.__tela_musica.mostra_mnsg("Artista não encontrado.")
            return

        genero: Genero = self.__controlador_sistema.controlador_genero.seleciona_genero(dados_musica["genero"])
        if genero is None:
            self.__tela_musica.mostra_mnsg("Gênero não encontrado.")
            return

        musica_existente = self.verificar_musica(dados_musica["nome_musica"], artista, genero)

        if musica_existente is not None:
            self.__tela_musica.mostra_mnsg("Essa música já está cadastrada.")
            return

        nova_musica = Musica(dados_musica["nome_musica"], artista, genero)
        self.__musica_dao.add(nova_musica.id_musica, nova_musica)
        self.__tela_musica.mostra_mnsg("Música criada com sucesso!")


    def verificar_musica(self, nome_musica, artista: Artista, genero: Genero):
        todas_musicas = self.__musica_dao.get_all()
        for musica in todas_musicas:
            if (musica.nome_musica == nome_musica and
                musica.artista == artista and
                musica.genero == genero):
                return musica
        return None


    def listar_musicas(self):
        musicas = self.__musica_dao.get_all()

        if not musicas:
            self.__tela_musica.mostra_mnsg("Não há músicas cadastradas.")
            return
        
        n_musica = 1
        for musica in musicas:
            genero = musica.genero.genero
            artista = musica.artista.nome_artistico


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
        
        musicas = self.__musica_dao.get_all()
        musicas_do_genero = []

        for musica in musicas:
            if musica.genero == genero:
                musicas_do_genero.append(musica)

        if not musicas_do_genero:
            self.__tela_musica.mostra_mnsg("Não há músicas com esse Gênero.")
            return

        n_musica = 1
        self.__tela_musica.mostra_mnsg(f"Músicas de: {genero.genero}")
        for musica in musicas_do_genero:
            artista = musica.artista.nome_artistico
            genero = musica.genero.genero
            self.__tela_musica.mostra_musica(n_musica,
                {"nome_musica": musica.nome_musica, "artista": artista, "genero": genero})
            n_musica += 1

    def pega_musica_genero(self):
        pega_genero = self.__tela_musica.selecionar_genero()
        genero = self.__controlador_sistema.controlador_genero.seleciona_genero(
            pega_genero)

        if genero is None:
            return 

        musicas = self.__musica_dao.get_all()
        musicas_do_genero = []

        for musica in musicas:
            if musica.genero == genero:
                musicas_do_genero.append(musica)

        if not musicas_do_genero:
            return 

        return musicas_do_genero

    def listar_musicas_por_artista(self):
        pega_artista = self.__tela_musica.seleciona_artista()
        artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(
            pega_artista)

        if artista is None:
            self.__tela_musica.mostra_mnsg("Não há músicas desse Artista.")
            return

        musicas = self.__musica_dao.get_all()
        musicas_do_artista = []

        for musica in musicas:
            if musica.artista == artista:
                musicas_do_artista.append(musica)

        if not musicas_do_artista:
            self.__tela_musica.mostra_mnsg("Não há músicas desse Artista.")
            return

        n_musica = 1
        self.__tela_musica.mostra_mnsg(f"Músicas de: {artista.nome_artistico}")
        for musica in musicas_do_artista:
            artista = musica.artista.nome_artistico
            genero = musica.genero.genero
            self.__tela_musica.mostra_musica(n_musica,
                {"nome_musica": musica.nome_musica, "artista": artista, "genero": genero})
            n_musica += 1

    def pega_musica_artista(self):
        pega_artista = self.__tela_musica.seleciona_artista()
        artista = self.__controlador_sistema.controlador_artista.pega_artista_por_nome(
            pega_artista)

        if artista is None:
            return 
        
        musicas = self.__musica_dao.get_all()
        musicas_do_artista = []

        for musica in musicas:
            if musica.artista == artista:
                musicas_do_artista.append(musica)

        if not musicas_do_artista:
            return 

        return musicas_do_artista


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_musica, 2: self.listar_musicas,
                        3: self.listar_musicas_por_genero, 4: self.listar_musicas_por_artista, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_musica.tela_opcoes()]()
