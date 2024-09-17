from pais import *
from estado import *
from cidade import *

# País

def pais_inserir(nome, abreviacao, moeda, populacao, nacionalidade):
    c = Pais(0, nome, abreviacao, moeda, populacao, nacionalidade)
    Paises.inserir(c)

def pais_listar():
    return Paises.listar()    

def pais_atualizar(id, nome, abreviacao, moeda, populacao, nacionalidade):
    c = Pais(id, nome, abreviacao, moeda, populacao, nacionalidade)
    Paises.atualizar(c)

def pais_excluir(id):
    c = Pais(id, "", "", "", "", "")
    Paises.excluir(c)    

# Estado:

def estado_inserir(nome, abreviacao, idpais):
    c = Estado(0, nome, abreviacao, idpais)
    Estados.inserir(c)
    

def estado_listar():
    return Estados.listar()    

def estado_atualizar(id, nome, abreviacao, idpais):
    c = Estado(id, nome, abreviacao, idpais)
    Estados.atualizar(c)

def estado_excluir(id):
    c = Estado(id, "", "", "")
    Estados.excluir(c)   

# Cidades

def cidade_inserir(nome, idestado):
    c = Cidade(0, nome, idestado)
    Cidades.inserir(c)

def cidade_listar():
    return Cidades.listar()    

def cidade_atualizar(id, nome, idestado):
    c = Cidade(id, nome, idestado)
    Cidades.atualizar(c)

def cidade_excluir(id):
    c = Cidade(id, "", "")
    Cidades.excluir(c)