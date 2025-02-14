import json
from Models.crud import CRUD

#Modelo
class Cidade:
    def __init__(self, id, nome, nat, populacao, idestado):
        self.__id = id
        self.__nome = nome
        self.__nat = nat
        self.__populacao = populacao
        self.__idestado = idestado
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_nat(self):
        return self.__nat
    def get_populacao(self):
        return self.__populacao
    def get_idestado(self):
        return self.__idestado
    
#Persistência
import json
from crud import CRUD


class Cidades (CRUD):
    @classmethod
    def salvar(cls):
        with open("cidades.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("cidades.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Cidade(obj["_Cidade__id"], obj["_Cidade__nome"], obj["_Cidade__nat"], obj["_Cidade__populacao"], obj["_Cidade__idestado"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass