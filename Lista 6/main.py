from cliente import *
from horario import *
from servico import *

class UI:
  @staticmethod
  def menu():
    print("1 - Inserir cliente, 2 - Listar clientes, 3 - atualizar cliente, 4 - excluir cliente, 5 - inserir horário, 6 - listar horarios, 7 - atualizar horários, 8 - excluir horário, 9 - inserir serviço, 10 - listar serviços, 11 - atualizar serviço, 12 - excluir serviço, 13 - Fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 13:
      op = UI.menu()
      if op == 1: UI.cliente_inserir()
      if op == 2: UI.cliente_listar()
      if op == 3: UI.cliente_atualizar()
      if op == 4: UI.cliente_excluir()
      if op == 5: UI.horario_inserir()
      if op == 6: UI.horario_listar()
      if op == 7: UI.horario_atualizar()
      if op == 8: UI.horario_excluir()
      if op == 9: UI.servico_inserir()
      if op == 10: UI.servico_listar()
      if op == 11: UI.servico_atualizar()
      if op == 12: UI.servico_excluir()

  @staticmethod
  def cliente_inserir():
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    fone = input("Informe o fone: ")
    c = Cliente(0, nome, email, fone)
    Clientes.inserir(c)

  @staticmethod
  def cliente_listar():  
    for c in Clientes.listar():
      print(c)

  @staticmethod
  def cliente_atualizar():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    fone = input("Informe o novo fone: ")
    c = Cliente(id, nome, email, fone)
    Clientes.atualizar(c)

  @staticmethod
  def cliente_excluir():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    c = Cliente(id, "", "", "")
    Clientes.excluir(c)

  @staticmethod
  def horario_inserir():
    #id = int(input("Informe o id: "))
    de = input("Informe a descrição: ")
    da = input("Informe a data (dd/mm/aaaa): ")
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
    UI.horario_listar()
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
    UI.horario_listar()
    id = int(input("Informe o id do horário a ser excluído: "))
    h = Horario(id, "", "", "", "", "")
    Horarios.excluir(h)

  @staticmethod
  def servico_inserir():
    #id = int(input("Informe o id: "))
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
    UI.servico_listar()
    id = int(input("Informe o ID a ser atualizado"))
    de = input("Informe a nova descrição: ")
    v = float(input("Informe o novo valor do serviço: "))
    d = float(input("Informe a nova duração do serviço: "))
    s = Servico(id, de, v, d)
    Servicos.atualizar(s)

  @staticmethod
  def servico_excluir():
    UI.servico_listar()
    id = int(input("Informe o id do serviço a ser excluído: "))
    s = Servico(id, "", "", "")
    Servicos.excluir(s)

UI.main()