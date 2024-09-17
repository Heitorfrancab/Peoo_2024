import json

class Pais:
    def __init__(self, id, nome, abreviacao, moeda, populacao, nacionalidade):
        self.id = id
        self.nome = nome
        self.abrev = abreviacao
        self.moed = moeda
        self.popu = populacao
        self.naci = nacionalidade
    def __str__(self):
        return f"ID: {self.id} - Nome: {self.nome} - Abreviação: {self.abrev} - Moeda: {self.moed} - População: {self.popu} - Nacionalidade: {self.naci}"

class Paises:
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
      c.moed = obj.moed
      c.popu = obj.popu
      c.naci = obj.naci
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
    with open("pais.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("pais.json", mode="r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:   
          c = Pais(obj["id"], obj["nome"], obj["abrev"], obj["moed"], obj["popu"], obj["naci"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass