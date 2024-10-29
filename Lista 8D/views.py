from cliente import *
from servico import *
from horario import *

class View:
  @staticmethod
  def cliente_inserir():
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    fone = input("Informe o fone: ")
    senha = input("Informe a senha: ")
    c = Cliente(0, nome, email, fone, senha)
    Clientes.inserir(c)

  @staticmethod
  def cliente_listar():  
    for c in Clientes.listar():
      print(c)

  @staticmethod
  def cliente_atualizar():
    View.cliente_listar()
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    fone = input("Informe o novo fone: ")
    senha = input("Informe o nova senha: ")
    c = Cliente(id, nome, email, fone, senha)
    Clientes.atualizar(c)

  @staticmethod
  def cliente_excluir():
    View.cliente_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    c = Cliente(id, "", "", "", "")
    Clientes.excluir(c)

  @staticmethod
  def horario_inserir():
    de = input("Informe a descrição: ")
    da = input("Informe a data (dd/mm/aaaa hh:mm): ")
    c = True
    idc = input("Informe o identificador do cliente: ")
    ids = input("Informe o identificador do serviço: ")
    h = Horario(0, de, da, c, idc, ids)
    Horarios.inserir(h)

  @staticmethod
  def horario_listar():  
    for h in Horarios.listar():
      print(h)

  @staticmethod
  def horario_atualizar():
    View.horario_listar()
    id = int(input("Informe o ID a ser atualizado"))
    de = input("Informe a nova descrição: ")
    da = input("Informe a nova data (dd/mm/aaaa): ")
    c = True
    idc = input("Informe o identificador do cliente: ")
    ids = input("Informe o identificador do serviço: ")
    h = Horario(id, de, da, c, idc, ids)
    Horarios.atualizar(h)

  @staticmethod
  def horario_excluir():
    View.horario_listar()
    id = int(input("Informe o id do horário a ser excluído: "))
    h = Horario(id, "", "", "", "", "")
    Horarios.excluir(h)

  @staticmethod
  def servico_inserir():
    de = input("Informe a descrição: ")
    v = float(input("Informe o valor do serviço: "))
    d = float(input("Informe a duração do serviço: "))
    s = Servico(0, de, v, d)
    Servicos.inserir(s)

  @staticmethod
  def servico_listar():  
    for s in Servicos.listar():
      print(s)

  @staticmethod
  def servico_atualizar():
    View.servico_listar()
    id = int(input("Informe o ID a ser atualizado"))
    de = input("Informe a nova descrição: ")
    v = float(input("Informe o novo valor do serviço: "))
    d = float(input("Informe a nova duração do serviço: "))
    s = Servico(id, de, v, d)
    Servicos.atualizar(s)

  @staticmethod
  def servico_excluir():
    View.servico_listar()
    id = int(input("Informe o id do serviço a ser excluído: "))
    s = Servico(id, "", "", "")
    Servicos.excluir(s)