from pais import *
from estado import *
from cidade import *

class View:
    # País

    @staticmethod
    def pais_inserir(nome, abreviacao, moeda, populacao, nacionalidade):
        c = Pais(0, nome, abreviacao, moeda, populacao, nacionalidade)
        Paises.inserir(c)
    @staticmethod
    def pais_listar():
        return Paises.listar()    
    @staticmethod
    def pais_atualizar(id, nome, abreviacao, moeda, populacao, nacionalidade):
        c = Pais(id, nome, abreviacao, moeda, populacao, nacionalidade)
        Paises.atualizar(c)
    @staticmethod
    def pais_excluir(id):
        c = Pais(id, "", "", "", "", "")
        Paises.excluir(c)    

    # Estado:

    @staticmethod
    def estado_inserir(nome, abreviacao, naturalidade, populacao, idpais):
        c = Estado(0, nome, abreviacao, naturalidade, populacao, idpais)
        Estados.inserir(c) 
    @staticmethod
    def estado_listar():
        return Estados.listar()    
    @staticmethod
    def estado_atualizar(id, nome, abreviacao, naturalidade, populacao, idpais):
        c = Estado(id, nome, abreviacao, naturalidade, populacao, idpais)
        Estados.atualizar(c)
    @staticmethod
    def estado_excluir(id):
        c = Estado(id, "", "", "", "", "")
        Estados.excluir(c)   

    # Cidades

    @staticmethod
    def cidade_inserir(nome, naturalidade, populacao, idestado):
        c = Cidade(0, nome, naturalidade, populacao, idestado)
        Cidades.inserir(c)
    @staticmethod
    def cidade_listar():
        return Cidades.listar()    
    @staticmethod
    def cidade_atualizar(id, nome, naturalidade, populacao, idestado):
        c = Cidade(id, nome, naturalidade, populacao, idestado)
        Cidades.atualizar(c)
    @staticmethod
    def cidade_excluir(id):
        c = Cidade(id, "", "", "", "")
        Cidades.excluir(c)