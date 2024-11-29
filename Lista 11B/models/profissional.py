import json

# Modelo
class Profissional:
  def __init__(self, id, nome, especialidade, conselho, email, senha):
    self.__id = id
    self.__nome = nome
    self.__especialidade = especialidade
    self.__conselho = conselho
    self.__email = email
    self.__senha = senha

    self.setid()
    self.setnome()
    self.setespecialidade()
    self.setconselho()
    self.setemail()
    self.setsenha()
  def setid(self):
    if self.__id < 0:
      raise ValueError("Id inválido. ")
  def setnome(self):
    if self.__nome == "" or self.__nome == " ":
      raise ValueError("Parâmetro de nome vazio. ")
  def setespecialidade(self):
    if self.__especialidade == "" or self.__especialidade == " ":
      raise ValueError("Parâmetro de identificador de especialidade vazio. ")
  def setconselho(self):
    if self.__conselho == "" or self.__conselho == " ":
      raise ValueError("Parâmetro de identificador de conselho vazio. ")
  def setemail(self):
    if self.__email == "" or self.__email == " ":
      raise ValueError("Parâmetro de identificador de email vazio. ")
  def setsenha(self):
    if self.__senha == "" or self.__senha == " ":
      raise ValueError("Parâmetro de identificador de profissional vazio. ")
  def getid(self):
    return self.__id
  def getnome(self):
    return self.__nome
  def getidespecialidade(self):
    return self.__especialidade
  def getconselho(self):
    return self.__conselho
  def getidemail(self):
    return self.__email
  def getsenha(self):
    return self.__senha
  def __str__(self):
    return f"{self.__nome} - {self.__especialidade} - {self.__conselho}"

# Persistência
class Profissionais:
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
      c.__especialidade = obj.__especialidade
      c.__conselho = obj.__conselho
      c.__email = obj.__email
      c.__senha = obj.__senha
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
    cls.objetos.sort(key=lambda profissional: profissional.nome)
    return cls.objetos

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