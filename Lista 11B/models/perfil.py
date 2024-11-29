import json

# Modelo
class Perfil:
  def __init__(self, id, nome, descricao, beneficio):
    self.__id = id
    self.__nome = nome
    self.__descricao = descricao
    self.__beneficio = beneficio
  def setid(self):
    if self.__id < 0:
      raise ValueError("Id inválido. ")
  def setnome(self):
    if self.__nome == "" or self.__nome == " ":
      raise ValueError("Parâmetro de nome vazio. ")
  def setdescricao(self):
    if self.__descricao == "" or self.__descricao == " ":
      raise ValueError("Parâmetro de descrição vazio. ")
  def setsenha(self):
    if self.__beneficio == "" or self.__beneficio == " ":
      raise ValueError("Parâmetro de benefício vazio. ")
  def __str__(self):
    return f"{self.__nome} - {self.__descricao} - {self.__beneficio}"

# Persistência
class Perfis:
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
    c = cls.listar_id(obj.id)
    if c != None:
      c.__nome = obj.__nome
      c.__descricao = obj.__descricao
      c.__beneficio = obj.__beneficio
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
    cls.objetos.sort(key=lambda Perfil: Perfil.nome)
    return cls.objetos

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