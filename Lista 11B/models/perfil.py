import json
from models.crud import *

# Modelo
class Perfil:
  def __init__(self, id, nome, descricao, beneficio):
    self.id = id
    self.nome = nome
    self.descricao = descricao
    self.beneficio = beneficio
  def __str__(self):
    return f"{self.nome} - {self.descricao} - {self.beneficio}"

# Persistência
class Perfis (CRUD):
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.descricao = obj.descricao
      c.beneficio = obj.beneficio
      cls.salvar()

  @classmethod
  def salvar(cls):
    with open("perfis.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("perfis.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Perfil(obj["id"], obj["nome"], obj["descricao"], obj["beneficio"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass