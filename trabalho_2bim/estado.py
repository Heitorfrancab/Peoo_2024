import json
from pais import *

class Estado:
    def __init__(self, id, nome, abreviacao, naturalidade, populacao, idpais):
        self.id = id
        self.nome = nome
        self.abrev = abreviacao
        self.natu = naturalidade
        self.popu = populacao
        self.idpais = idpais
    
    def __str__(self):
        return f"ID estado: {self.id} - Nome do estado: {self.nome}, Abreviação do estado: {self.abrev} - Naturalidade do estado: {self.natu} - População do estado: {self.popu} - ID país: {self.idpais}"
    
class Estados:
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
      c.abrev = obj.abrev
      c.natu = obj.natu
      c.popu = obj.popu
      c.idpais = obj.idpais
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
    with open("estados.json", mode="w") as arquivo:
        json.dump([vars(obj) for obj in cls.objetos], arquivo, indent=4)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("estados.json", mode="r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:   
          c = Estado(obj["id"], obj["nome"], obj["abrev"], obj["natu"], obj["popu"], obj["idpais"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass