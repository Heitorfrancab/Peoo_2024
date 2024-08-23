import json

class Servico:
    def __init__(self, id, de, v, du):
        self.__id = id
        self.__description = de
        self.__value = v
        self.__duration = du

        self.set_id()
        self.set_value()
        self.set_duration()
    def set_id(self):
        if self.__id >= 0:
            pass
        else:
            raise ValueError()
    def set_value(self):
        if self.__value >= 0:
            pass
        else:
            raise ValueError()
    def set_duration(self):
        if self.__duration >= 0:
            pass
        else:
            raise ValueError()
    def get_id(self):
        return self.__id
    def get_description(self):
        return self.__description
    def get_value(self):
        return self.__value
    def get_duration(self):
        return self.__duration

class Servicos:
    servicos = []
    @classmethod
    def inserir(cls, obj):
        m = 0
        for c in cls.servicos:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.servicos.append(obj)
    @classmethod
    def listar_id(cls, id):
        for c in cls.servicos:
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
            cls.servicos.remove(c)
    @classmethod
    def listar(cls):
        for x in range(0, len(cls.servicos)):
            print(cls.servicos[x])
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:   # w - write
            json.dump(cls.servicos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.servicos = []
        with open("clientes.json", mode="r") as arquivo:   # r - read
            texto = json.load(arquivo)
            for obj in texto:   
                c = Servico(obj["ID"], obj["Date"], obj["Confirmation"], obj["Client ID"], obj["Service ID"])
                cls.servicos.append(c)