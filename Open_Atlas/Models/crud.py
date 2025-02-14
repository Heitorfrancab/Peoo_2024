from abc import abstractmethod
import json

class CRUD:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.get_id() >= m: m = c.get_id()
    obj.set_id(m + 1)
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.get_id() == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.get_id())
    if c != None:
      cls.objetos.remove(c)
      cls.objetos.append(obj)      
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_id())
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    cls.objetos.sort(key=lambda obj: obj.get_id())
    return cls.objetos

  @abstractmethod
  def salvar(cls):
    with open("crud.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @abstractmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("crud.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = None
          cls.objetos.append(c)
    except FileNotFoundError:
      pass