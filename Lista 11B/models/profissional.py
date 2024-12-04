import json
from models.crud import *

# Modelo
class Profissional:
  def __init__(self, id, nome, especialidade, conselho, email, senha):
    self.id = id
    self.nome = nome
    self.especialidade = especialidade
    self.conselho = conselho
    self.email = email
    self.senha = senha
  def __str__(self):
    return f"{self.nome} - {self.especialidade} - {self.conselho}"

# Persistência
class Profissionais (CRUD):
  objetos = []    # atributo estático
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.especialidade = obj.especialidade
      c.conselho = obj.conselho
      c.email = obj.email
      c.senha = obj.senha
      cls.salvar()

  @classmethod
  def salvar(cls):
    with open("profissionais.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("profissionais.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Profissional(obj["id"], obj["nome"], obj["especialidade"], obj["conselho"], obj["email"], obj["senha"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass