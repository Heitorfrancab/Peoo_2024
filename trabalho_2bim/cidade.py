import json
from estado import *

class Cidade:
  def __init__(self, id, nome, naturalidade, populacao, idestado):
    self.id = id
    self.nome = nome
    self.natu = naturalidade
    self.popu = populacao
    self.idestado = idestado
  def __str__(self):
    return f"ID da cidade: {self.id} - Nome da cidade: {self.nome} - Naturalidade da cidade: {self.natu} - População da cidade: {self.popu} - ID do estado: {self.idestado}"

class Cidades:
  objetos = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.id > m: m = c.id
    obj.id = m + 1
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.natu = obj.natu
      c.popu = obj.popu
      c.idestado = obj.idestado
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("cidades.json", mode="w") as arquivo:  
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("cidades.json", mode="r") as arquivo:   
        texto = json.load(arquivo)
        for obj in texto:   
          c = Cidade(obj["id"], obj["nome"], obj["natu"], obj["popu"], obj["idestado"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass