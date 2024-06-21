from typing import List
from entidades.usuario import Usuario
from tela.telausuario import TelaUsuario


class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__lista_usuarios: List[Usuario] = list()
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    def pega_usuario_por_nome_usuario(self, nome_usuario: str):
        for usuario in self.__lista_usuarios:
            if usuario.nome_usuario == nome_usuario:
                return usuario
        return None

    # 1
    def criar_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        novo_usuario = Usuario(
            dados_usuario["nome"], dados_usuario["nome_usuario"], dados_usuario["email"], dados_usuario["telefone"])
        nome_de_usuario_existente = False
        for usuario in self.__lista_usuarios:
            if usuario.nome_usuario == dados_usuario["nome_usuario"]:
                nome_de_usuario_existente = True
                break
        if not nome_de_usuario_existente:
            self.__lista_usuarios.append(novo_usuario)
            self.__tela_usuario.mostra_mensagem("Usuário criado com sucesso!")
        else:
            self.__tela_usuario.mostra_mensagem("Esse nome de usuário não está disponível")

    # 2
    def excuir_usuario(self):
        self.listar_usuarios()
        usuario_excluir = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_nome_usuario(usuario_excluir) # type: ignore

        if (usuario is not None):
            self.__lista_usuarios.remove(usuario)
            self.__tela_usuario.mostra_mensagem("Usuario removido com sucesso")
        else:
            self.__tela_usuario.mostra_mensagem(
                "Este Nome de Usuario não existe")

    # 3
    def listar_usuarios(self):
        self.__tela_usuario.mostra_mensagem("Lista de Usuarios: ")
        for usuario in self.__lista_usuarios:
            self.__tela_usuario.mostrar_usuario(
                {"nome": usuario.nome, "nome_usuario": usuario.nome_usuario, "email": usuario.email, "telefone": usuario.telefone})
            

    # 4
    def adicionar_musicas_preferidas(self):
        dados_usuario = self.__tela_usuario.seleciona_usuario()
        musicas_preferidas = self.__tela_usuario.musicas_preferidas()
        usuario = self.pega_usuario_por_nome_usuario(dados_usuario["nome"])

        if usuario is None:
            self.__tela_usuario.mostra_mensagem("Usuario Invalido")
            return

        for valor in musicas_preferidas.values():
            usuario.musicas_preferidas.append(valor)
        
        self.__tela_usuario.mostra_mensagem("As musicas favoritas foram adicionadas!")

    # 5
    def adicionar_amizades(self):
        dados_amizade = self.__tela_usuario.fazer_amizade()
        dados_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_nome_usuario(dados_usuario) # type: ignore
        amigo = self.pega_usuario_por_nome_usuario(dados_amizade) # type: ignore

        if usuario is None or amigo is None:
            self.__tela_usuario.mostra_mensagem(
                "Pelo menos um dos nomes de usuário não existe.")
            return

        usuario.amizades.append(amigo)
        amigo.amizades.append(usuario)

        self.__tela_usuario.mostra_mensagem("Amizade adicionada com sucesso.")

    # 6
    def ver_amizades(self):

        nome_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_nome_usuario(nome_usuario) # type: ignore
        if usuario in self.__lista_usuarios:
            self.__tela_usuario.mostra_mensagem("Meus amigos: ")
            for amizade in usuario.amizades:
                nome_amigo = amizade.nome_usuario
                self.__tela_usuario.mostra_mensagem(nome_amigo)

    
    #7
    def ver_musicas_favoritas_amigos(self):
        nome_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_nome_usuario(nome_usuario) # type: ignore

        if usuario is None:
            self.__tela_usuario.mostra_mensagem("Usuário não encontrado.")
            return

        nome_amigo = self.__tela_usuario.fazer_amizade()
        amigo = self.pega_usuario_por_nome_usuario(nome_amigo) # type: ignore

        if amigo is None:
            self.__tela_usuario.mostra_mensagem("Amigo não encontrado.")
            return
        
        if amigo in usuario.amizades:
            self.__tela_usuario.mostra_mensagem("Músicas favoritas de " + nome_amigo + ":") # type: ignore
            for musica in amigo.musicas_preferidas:
                self.__tela_usuario.mostra_mensagem("- " + musica)
        else:
            self.__tela_usuario.mostra_mensagem(nome_amigo + " não é seu amigo.") # type: ignore






    # 0
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_usuario, 2: self.excuir_usuario, 3: self.listar_usuarios, 4: self.adicionar_musicas_preferidas,
                        5: self.adicionar_amizades, 6: self.ver_amizades, 7: self.ver_musicas_favoritas_amigos ,8: self.retornar}

        while True:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()
