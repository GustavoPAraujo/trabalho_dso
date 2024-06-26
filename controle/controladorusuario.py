from entidades.usuario import Usuario
from tela.telausuario import TelaUsuario
from DAOs.usuario_dao import UsuarioDao


class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema
        self.__usuario_dao = UsuarioDao()


    def pega_usuario_por_nome_usuario(self, nome_usuario: str):
        return self.__usuario_dao.get(nome_usuario)

    # 1
    def criar_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()

        if self.__usuario_dao.get(dados_usuario["nome_usuario"]) is None:
            novo_usuario = Usuario(dados_usuario["nome"], dados_usuario["nome_usuario"], dados_usuario["email"], dados_usuario["telefone"])
            self.__usuario_dao.add(novo_usuario.nome_usuario, novo_usuario)
            self.__tela_usuario.mostra_mensagem("Usuário criado com sucesso!")
        else:
            self.__tela_usuario.mostra_mensagem("Esse nome de usuário não está disponível")

    # 2
    def excuir_usuario(self):
        self.listar_usuarios()
        usuario_excluir = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_nome_usuario(usuario_excluir["nome_usuario"])

        if usuario is not None:
            self.__usuario_dao.remove(usuario.nome_usuario)
            self.__tela_usuario.mostra_mensagem("Usuário removido com sucesso")
        else:
            self.__tela_usuario.mostra_mensagem("Este nome de usuário não existe")

    # 3
    def listar_usuarios(self):
        self.__tela_usuario.mostra_mensagem("Lista de Usuários:")
        usuarios = self.__usuario_dao.get_all()
        for usuario in usuarios:
            dados_usuario = {
                "nome": usuario.nome,
                "nome_usuario": usuario.nome_usuario,
                "email": usuario.email,
                "telefone": usuario.telefone
            }
            self.__tela_usuario.mostrar_usuario(dados_usuario)
    # 4
    def adicionar_musicas_preferidas(self):
        dados_usuario = self.__tela_usuario.seleciona_usuario()
        musicas_preferidas = self.__tela_usuario.musicas_preferidas()
        usuario = self.pega_usuario_por_nome_usuario(dados_usuario["nome_usuario"])

        if usuario is None:
            self.__tela_usuario.mostra_mensagem("Usuário inválido")
            return

        for valor in musicas_preferidas.values():
            usuario.musicas_preferidas.append(valor)

        self.__usuario_dao.update(usuario.nome_usuario, usuario)
        self.__tela_usuario.mostra_mensagem("As músicas favoritas foram adicionadas!")

    # 5
    def adicionar_amizades(self):
        dados_amizade = self.__tela_usuario.fazer_amizade()
        dados_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_nome_usuario(dados_usuario["nome_usuario"])
        amigo = self.pega_usuario_por_nome_usuario(dados_amizade["amigo"])

        if usuario is None or amigo is None:
            self.__tela_usuario.mostra_mensagem("Pelo menos um dos nomes de usuário não existe.")
            return

        usuario.amizades.append(amigo)
        amigo.amizades.append(usuario)

        self.__usuario_dao.update(usuario.nome_usuario, usuario)
        self.__usuario_dao.update(amigo.nome_usuario, amigo)

        self.__tela_usuario.mostra_mensagem("Amizade adicionada com sucesso.")

    # 6
    def ver_amizades(self):
        nome_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_nome_usuario(nome_usuario["nome_usuario"])

        if usuario is None:
            self.__tela_usuario.mostra_mensagem("Usuário não encontrado.")
            return

        self.__tela_usuario.mostra_mensagem("Meus amigos:")
        for amizade in usuario.amizades:
            nome_amigo = amizade.nome_usuario
            self.__tela_usuario.mostra_mensagem(nome_amigo)

    
    #7
    def ver_musicas_favoritas_amigos(self):
        nome_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_nome_usuario(nome_usuario["nome_usuario"])

        if usuario is None:
            self.__tela_usuario.mostra_mensagem("Usuário não encontrado.")
            return

        nome_amigo = self.__tela_usuario.fazer_amizade()
        amigo = self.pega_usuario_por_nome_usuario(nome_amigo["nome_usuario"])

        if amigo is None:
            self.__tela_usuario.mostra_mensagem("Amigo não encontrado.")
            return

        if amigo in usuario.amizades:
            self.__tela_usuario.mostra_mensagem("Músicas favoritas de " + nome_amigo["amigo"] + ":")
            for musica in amigo.musicas_preferidas:
                self.__tela_usuario.mostra_mensagem("- " + musica)
        else:
            self.__tela_usuario.mostra_mensagem(nome_amigo["amigo"] + " não é seu amigo.")

    # 0
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_usuario, 2: self.excuir_usuario, 3: self.listar_usuarios, 4: self.adicionar_musicas_preferidas,
                        5: self.adicionar_amizades, 6: self.ver_amizades, 7: self.ver_musicas_favoritas_amigos ,8: self.retornar}

        while True:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()
