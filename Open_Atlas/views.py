from Models.cidade import *
from Models.crud import *
from Models.estado import *
from Models.pais import *
from Models.usuario import *

class View:
    def usuario_admin():
        for c in View.usuario_listar():
            if c.email == "admin": return
        View.usuario_inserir("admin", "admin", "1234", "1234")
    def usuario_autenticar(email, senha):
        for c in View.usuario_listar():
            if c.get_email == email and c.get_senha == senha:
                return {"id" : c.get_id, "nome" : c.get_nome}
        return None


    def usuario_inserir(email, nome, senha):
        c = Usuario(0, email, nome, senha)
        Usuarios.inserir(c)
    def usuario_listar():
        return Usuarios.listar()
    def cliente_listar_id(id):
        return Usuarios.listar_id(id)   
    def usuario_atualizar(id, email, nome, senha):
        c = Usuario(id, email, nome, senha)
        Usuarios.atualizar(c)
    def usuario_excluir(id):
        c = Usuario(id, "", "", "")
        Usuarios.excluir(c)

    
    
    def cidade_inserir(nome, nat, populacao, idestado):
        c = Cidade(0, nome, nat, populacao, idestado)
        Cidades.inserir(c)
    def usuario_listar():
        return Cidades.listar()
    def cliente_listar_id(id):
        return Cidades.listar_id(id)   
    def usuario_atualizar(id, nome, nat, populacao, idestado):
        c = Cidade(id, nome, nat, populacao, idestado)
        Cidades.atualizar(c)
    def usuario_excluir(id):
        c = Cidade(id, "", "", "", "")
        Cidades.excluir(c)



    def estado_inserir(nome, nat, populacao, idestado):
        c = Estado(0, nome, nat, populacao, idestado)
        Estados.inserir(c)
    def estado_listar():
        return Estados.listar()
    def estado_listar_id(id):
        return Estados.listar_id(id)   
    def estado_atualizar(id, nome, nat, populacao, idestado):
        c = Estado(id, nome, nat, populacao, idestado)
        Cidades.atualizar(c)
    def estado_excluir(id):
        c = Estado(id, "", "", "", "")
        Estados.excluir(c)



    def pais_inserir(nome, nat, populacao, idestado):
        c = Pais(0, nome, nat, populacao, idestado)
        Paises.inserir(c)
    def pais_listar():
        return Paises.listar()
    def pais_listar_id(id):
        return Paises.listar_id(id)   
    def pais_atualizar(id, nome, nat, populacao, idestado):
        c = Pais(id, nome, nat, populacao, idestado)
        Paises.atualizar(c)
    def pais_excluir(id):
        c = Pais(id, "", "", "", "")
        Paises.excluir(c)