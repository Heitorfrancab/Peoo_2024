import json
from datetime import *

class Horario:
    def __init__(self, id, d, c, idc, ids):
        self.__id = id
        self.__date = d
        self.__confirmed = c
        self.__idc = idc
        self.__ids = ids

        self.set_id()
    def set_id(self):
        if self.__id >= 0:
            pass
        else:
            raise ValueError()
    def get_id(self):
        return self.__id
    def get_date(self):
        return self.__date
    def get_confirmation(self):
        return self.__confirmed
    def get_client_id(self):
        return self.__idc
    def get_service_id(self):
        return self.__ids
    def __str__(self):
        return f'ID: {self.__id}\nDate: {self.__date}\nConfirmation: {self.__confirmed}\nClient ID: {self.__idc}\nService ID: {self.__ids}'
        

class Horarios:
    horarios = []
    @classmethod
    def inserir(cls, obj):
        m = 0
        for c in cls.horarios:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.horarios.append(obj)
    @classmethod
    def listar_id(cls, id):
        for c in cls.horarios:
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
            cls.horarios.remove(c)
    @classmethod
    def listar(cls):
        for x in range(0, len(cls.horarios)):
            print(cls.horarios[x])
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:   # w - write
            json.dump(cls.horarios, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.horarios = []
        with open("clientes.json", mode="r") as arquivo:   # r - read
            texto = json.load(arquivo)
            for obj in texto:   
                c = Horario(obj["ID"], obj["Date"], obj["Confirmation"], obj["Client ID"], obj["Service ID"])
                cls.horarios.append(c)
