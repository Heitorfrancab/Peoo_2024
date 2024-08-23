from clientes import *
from horarios import *
from servicos import *

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = UI.menu()
            if op == 1: UI.inserircliente()
            if op == 2: UI.listarcliente()
            if op == 3: UI.acessarcliente()
            if op == 4: UI.salvarcliente()
            if op == 5: UI.abrircliente()

    @staticmethod
    def menu():
        print("1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Acessar cliente")
        print("4 - Salvar JSON")
        print("5 - Abrir JSON")
        print("6 - Fim")
        return int(input("Escolha a opção: "))

    @staticmethod
    def inserircliente():
        id = int(input("Informar ID: "))
        n = input("Informar nome: ")
        e = input("Informar e-mail: ")
        f = input("Informar telefone: ")

        x = Cliente(id, n, e, f)

        Clientes.inserir(x)
    @staticmethod
    def listarcliente():
        Clientes.listar()
    @staticmethod
    def acessarcliente():
        id = int(input("Informar ID desejado"))

        Clientes.listar_id(id)
    @staticmethod
    def salvarcliente():
        Clientes.salvar(Clientes)
    @staticmethod
    def abrircliente():
        Clientes.abrir(Clientes)

UI.main()