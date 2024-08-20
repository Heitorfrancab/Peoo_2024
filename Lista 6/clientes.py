import json

class Cliente:
    def __init__(self, id, n, e, f):
        self.__id = id
        self.__n = n
        self.__e = e
        self.__f = f

        self.set_id()
    def set_id(self):
        if self.__id >= 0:
            pass
        else:
            raise ValueError()
    def __str__(self):
        return f'ID: {self.__id}; Nome: {self.__n}; Email: {self.__e}; Telefone: {self.__f}'

class Clientes:
    clientes = []
    @classmethod
    def inserir(cls, c):
        cls.clientes.append(c)
    @classmethod
    def listar(cls):
        for x in range(0, len(cls.clientes)):
            print(cls.clientes[x])
    @classmethod
    def listar_id(cls, id):
        print(cls.clientes[id]) 
    def abrir(cls):
        with open("clientes.json", mode="r") as arquivo:
            texto = json.load(arquivo)

            for obj in texto:
                c = Cliente(obj["id"], obj["nome"])
                cls.clientes.append(c)
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.clientes, arquivo, default = vars)

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.acessar()
            if op == 4: UI.salvar()
            if op == 5: UI.abrir()

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
    def inserir():
        id = int(input("Informar ID: "))
        n = input("Informar nome: ")
        e = input("Informar e-mail: ")
        f = input("Informar telefone: ")

        x = Cliente(id, n, e, f)

        Clientes.inserir(x)
    @staticmethod
    def listar():
        Clientes.listar()
    @staticmethod
    def acessar():
        id = int(input("Informar ID desejado"))

        Clientes.listar_id(id)
    @staticmethod
    def salvar():
        Clientes.salvar(Clientes)
    @staticmethod
    def abrir():
        Clientes.abrir(Clientes)

UI.main()