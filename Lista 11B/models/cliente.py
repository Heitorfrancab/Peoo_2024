# Lista de Clientes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json

# Modelo
class Cliente:
  def __init__(self, id, nome, email, fone, senha):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
    self.__senha = senha

    self.setid()
    self.setnome()
    self.setemail()
    self.setfone()
    self.setsenha()
  def setid(self):
    if self.__id < 0:
      raise ValueError("Id inválido. ")
  def setnome(self):
    if self.__nome == "" or self.__nome == " ":
      raise ValueError("Parâmetro de nome vazio. ")
  def setemail(self):
    if self.__email == "" or self.__email == " ":
      raise ValueError("Parâmetro de email vazio. ")
  def setfone(self):
    if self.__fone == "" or self.__fone == " ":
      raise ValueError("Parâmetro de telefone vazio. ")
  def setsenha(self):
    if self.__senha == "" or self.__senha == " ":
      raise ValueError("Parâmetro de senha vazio. ")
  def getid(self):
    return self.__id
  def getnome(self):
    return self.__nome
  def getemail(self):
    return self.__email
  def getsenha(self):
    return self.__senha
  def __str__(self):
    return f"{self.__nome} - {self.__email} - {self.__fone}"

# Persistência
class Clientes:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.__id > m: m = c.__id
    obj.__id = m + 1
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.__id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.__id)
    if c != None:
      c.__nome = obj.__nome
      c.__email = obj.__email
      c.__fone = obj.__fone
      c.__senha = obj.__senha
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.__id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    cls.objetos.sort(key=lambda cliente: cliente.nome)
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass