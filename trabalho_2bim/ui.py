import views

class UI:
  @staticmethod
  def menu():
    print("Cadastro de Países")
    print("  1 - Inserir, 2 - Listar, 3 - Atualizar , 4 - Excluir")
    print("Cadastro de Estados")
    print("  5 - Inserir, 6 - Listar, 7 - Atualizar , 8 - Excluir")
    print("Cadastro de Cidades")
    print("  9 - Inserir, 10 - Listar, 11 - Atualizar , 12 - Excluir")
    print("Outras opções")
    print("13- Fim")

    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 13:
      op = UI.menu()
      if op == 1: UI.pais_inserir()
      if op == 2: UI.pais_listar()
      if op == 3: UI.pais_atualizar()
      if op == 4: UI.pais_excluir()
      if op == 5: UI.estado_inserir()
      if op == 6: UI.estado_listar()
      if op == 7: UI.estado_atualizar()
      if op == 8: UI.estado_excluir()
      if op == 9: UI.cidade_inserir()
      if op == 10: UI.cidade_listar()
      if op == 11: UI.cidade_atualizar()
      if op == 12: UI.cidade_excluir()

  @staticmethod
  def pais_inserir():
    nome = input("Informe o nome: ")
    abreviacao = input("Informe a abreviação: ")
    moeda = input("Informe a moeda: ")
    populacao = int(input("Informe a população: "))
    nacionalidade = input("Informe a nacionalidade: ")
    views.pais_inserir(nome, abreviacao, moeda, populacao, nacionalidade)

  @staticmethod
  def pais_listar():  
    for c in views.pais_listar():
      print(c)
    
  @staticmethod
  def pais_atualizar():
    UI.pais_listar()
    id = int(input("Informe o id do país a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    abreviacao = input("Informe a nova abreviação: ")
    moeda = input("Informe a nova moeda: ")
    populacao = int(input("Informe a nova população: "))
    nascionalidade = input("Informe a nova nascionalidade: ")
    views.pais_atualizar(id, nome, abreviacao, moeda, populacao, nascionalidade)

  @staticmethod
  def pais_excluir():
    UI.pais_listar()
    id = int(input("Informe o id do país a ser excluído: "))
    views.pais_excluir(id)

  @staticmethod
  def estado_inserir():
    try:
        nome = input("Informe o nome: ")
        abreviacao = input("Informe a abreviação: ")
        UI.pais_listar()
        idpais = int(input("Qual o id do país que está este estado? (responda somente com o número)"))
        views.estado_inserir(nome, abreviacao, idpais)
    except Exception as e:
        print(f"Ocorreu um erro ao inserir o estado: {e}")

  @staticmethod
  def estado_listar():  
    for c in views.estado_listar():
      print(c)

  @staticmethod
  def estado_atualizar():
    UI.estado_listar()
    id = int(input("Informe o id do estado a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    abreviacao = input("Informe a nova abreviação: ")
    UI.pais_listar
    idpais = input("Informe o novo id do país deste estado: ")
    views.estado_atualizar(id, nome, abreviacao, idpais)

  @staticmethod
  def estado_excluir():
    UI.estado_listar()
    id = int(input("Informe o id do estado a ser excluído: "))
    views.estado_excluir(id)

  @staticmethod
  def cidade_inserir():
    nome = input("Informe o nome: ")
    UI.estado_listar()
    idestado = int(input("Qual o id do estado que está esta cidade? (responda somente com o número): "  ))
    views.cidade_inserir(nome, idestado)

  @staticmethod
  def cidade_listar():  
    for c in views.cidade_listar():
      print(c)

  @staticmethod
  def cidade_atualizar():
    UI.cidade_listar()
    id = int(input("Informe o id da cidade a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    UI.estado_listar
    idestado = input("Informe o novo id do estado desta cidade: ")
    views.cidade_atualizar(id, nome, idestado)

  @staticmethod
  def cidade_excluir():
    UI.cidade_listar()
    id = int(input("Informe o id da cidade a ser excluído: "))
    views.cidade_excluir(id)
UI.main()