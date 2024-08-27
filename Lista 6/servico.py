import json

class Servico:
  def __init__(self, id, de, v, d):
    self.id = id
    self.descricao = de
    self.value = v
    self.duration = d
  def __str__(self):
    return f"{self.id} - {self.descricao} - {self.value} - {self.duration}"

class Servicos:
  servicos = []
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for s in cls.servicos:
      if s.id > m: m = s.id
    obj.id = m + 1
    cls.servicos.append(obj)
    cls.salvar()
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.servicos:
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    s = cls.listar_id(obj.id)
    if s != None:
      s.descricao = obj.descricao
      s.value = obj.value
      s.duration = obj.duration
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    s = cls.listar_id(obj.id)
    if s != None:
      cls.servicos.remove(s)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.servicos
  @classmethod
  def salvar(cls):
    with open("servicos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.servicos, arquivo, default = vars)
  @classmethod
  def abrir(cls):
    cls.servicos = []
    try:
      with open("servicos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          s = Servico(obj["id"], obj["descricao"], obj["value"], obj["duration"])
          cls.servicos.append(s)
    except FileNotFoundError:
      pass