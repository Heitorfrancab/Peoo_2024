import json
from datetime import datetime

class Horario:
  def __init__(self, id, de, da, c, idc, ids):
    self.id = id
    self.descricao = de
    self.date = datetime.strptime(da, "%d/%m/%Y %H:%M")
    self.confirmed = c
    self.idc = idc
    self.ids = ids
  def __str__(self):
    return f"{self.id} - {self.descricao} - {self.date} - {self.confirmed} - {self.idc} - {self.ids}"
  def to_json(self):
    dic = {}
    dic["id"] = self.id
    dic["descricao"] = self.descricao
    dic["date"] = datetime.strftime(self.date, "%d/%m/%Y %H:%M")
    dic["confirmed"] = self.confirmed
    dic["idc"] = self.idc
    dic["ids"] = self.ids

    return(dic)

class Horarios:
  horarios = []
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.horarios:
      if c.id > m: m = c.id
    obj.id = m + 1
    cls.horarios.append(obj)
    cls.salvar()
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.horarios:
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    h = cls.listar_id(obj.id)
    if h != None:
      h.descricao = obj.descricao
      h.date = obj.date
      h.confirmed = obj.confirmed
      h.idc = obj.idc
      h.ids = obj.ids
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.horarios.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.horarios
  @classmethod
  def salvar(cls):
    with open("horarios.json", mode="w") as arquivo:
      json.dump(cls.horarios, arquivo, default = Horario.to_json)
  @classmethod
  def abrir(cls):
    cls.horarios = []
    try:
      with open("horarios.json", mode="r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:   
          h = Horario(obj["id"], obj["de"], datetime.strptime(obj["date"], "%d/%m/%Y %H:%M"), obj["c"], obj["idc"], obj["ids"])
          cls.horarios.append(h)
    except FileNotFoundError:
      pass