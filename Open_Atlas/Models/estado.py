import json
from Models.crud import CRUD

#Modelo
class Estado:
    def __init__(self, id, nome, abrev, nat, populacao, idpais):
        self.__id = id
        self.__nome = nome
        self.__abrev = abrev
        self.__nat = nat
        self.__populacao = populacao
        self.__idpais = idpais
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_abrev(self):
        return self.__abrev
    def get_nat(self):
        return self.__nat
    def get_populacao(self):
        return self.__populacao
    def get_idpais(self):
        return self.__idpais
    def __dict__(self):
        {'ID' : self.__id, 'Nome' : self.__nome, 'Abreviação' : self.__abrev, 'Naturalidade' : self.__nat, 'População' : self.__populacao, 'ID_Pais': self.__idpais}

#Persistência
class Estados (CRUD):
    @classmethod
    def salvar(cls):
        with open("estados.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("estados.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Estado(obj["_Estado__id"], obj["_Estado__nome"], obj["_Estado__abrev"], obj["_Estado__nat"], obj["_Estado__populacao"], obj["_Estado__idpais"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass