import json

# Modelo
class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.__id = id
    self.__descricao = descricao
    self.__valor = valor
    self.__duracao = duracao

    self.setid()
    self.setdescricao()
    self.setvalor()
    self.setduracao()
  def setid(self):
    if self.__id < 0:
      raise ValueError("Id inválido. ")
  def setdescricao(self):
    if self.__descricao == "" or self.__descricao == " ":
      raise ValueError("Parâmetro de descrição vazio. ")
  def setvalor(self):
    if self.__valor < 0:
      raise ValueError("Valor inválido. ")
  def setduracao(self):
    if self._duracao < 0:
      raise ValueError("Duração inválida. ")
  def getid(self):
    return self.__id
  def getdescricao(self):
    return self.__descricao
  def getvalor(self):
    return self.__valor
  def getduracao(self):
    return self.__duracao
  def __str__(self):
    return f"{self.__id} - {self.__descricao} - R$ {self.__valor:.2f} - {self.__duracao} min"

# Persistência
class Servicos:
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
      c.__descricao = obj.__descricao
      c.__valor = obj.__valor
      c.__duracao = obj.__duracao
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
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("servicos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("servicos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass