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
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__n
    def get_email(self):
        return self.__e
    def get_fone(self):
        return self.__f
    def __str__(self):
        return f'ID: {self.__id}; Nome: {self.__n}; Email: {self.__e}; Telefone: {self.__f}'


class Clientes:
    clientes = []
    @classmethod
    def inserir(cls, obj):
        m = 0
        for c in cls.clientes:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.clientes.append(obj)
    @classmethod
    def listar_id(cls, id):
        for c in cls.clientes:
            if c.id == id: return c
            else: return None  
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.email = obj.email
            c.fone = obj.fone
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.clientes.remove(c)
    @classmethod
    def listar(cls):
        for x in range(0, len(cls.clientes)):
            print(cls.clientes[x])
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:   # w - write
            json.dump(cls.clientes, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.clientes = []
        with open("clientes.json", mode="r") as arquivo:   # r - read
            texto = json.load(arquivo)
            for obj in texto:   
                c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                cls.clientes.append(c)