from sklearn.linear_model import MultiTaskElasticNet
from usuario import Usuario
from telausuario import TelaUsuario


class ControladorUsuario:
    def __init__(self) -> None:
        self.__lista_usuarios = []
        self.__tela_usuario = TelaUsuario()

    def pega_usuario_por_nome_usuario(self, nome_usuario: str):
        for usuario in self.__lista_usuarios:
            if usuario.nome_usuario == nome_usuario:
                return usuario
        return None

    def criar_usuario(self):  
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        novo_usuario = Usuario( dados_usuario["nome"], dados_usuario["nome_usuario"], dados_usuario["email"], dados_usuario["telefone"])
        if novo_usuario not in self.__lista_usuarios:
            self.__lista_usuarios.append(novo_usuario)

    def listar_usuarios(self):
        for usuario in self.__lista_usuarios:
            self.__tela_usuario.mostrar_usuario({"nome": usuario.nome ,"nome_usuario": usuario.nome_usuario, "email": usuario.email, "telefone": usuario.telefone})

    def excuir_usuario(self):
        self.listar_usuarios()
        usuario_excluir = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_nome_usuario(usuario_excluir)

        if (usuario is not None):
            self.__lista_usuarios.remove(usuario)
            self.listar_usuarios
        else:
            self.__tela_usuario.mostra_mensagem("Este Nome de Usuario não existe")
    
    def adicionar_amizades(self):
        dados_amizade = self.__tela_usuario.fazer_amizade()
        dados_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_nome_usuario(dados_usuario)
        amigo = self.pega_usuario_por_nome_usuario(dados_amizade)

        if usuario is None or amigo is None:
            self.__tela_usuario.mostra_mensagem("Pelo menos um dos nomes de usuário não existe.")
            return

        usuario.amizades.append(amigo)
        amigo.amizades.append(usuario)

        self.__tela_usuario.mostra_mensagem("Amizade adicionada com sucesso.")

           
    def adicionar_musicas_preferidas(self):
        dados_usuario = self.__tela_usuario.seleciona_usuario()
        musicas_preferidas = self.__tela_usuario.musicas_preferidas()
        usuario = self.pega_usuario_por_nome_usuario(dados_usuario)

        if usuario is None:
            self.__tela_usuario.mostra_mensagem("Usuario Invãlido")
            return

        for valor in musicas_preferidas.values():
            usuario.musicas_preferidas.append(valor)
