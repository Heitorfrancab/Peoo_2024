import json
from Models.crud import CRUD

class Pais:
    def __init__(self, id, nome, abrev, nac, moeda, populacao, capital, cod):
        self.__id = id
        self.__nome = nome
        self.__abrev = abrev
        self.__nac = nac
        self.__moeda = moeda
        self.__populacao = populacao
        self.__capitalid = capital
        self.__cod = cod
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_abrev(self):
        return self.__abrev
    def get_nac(self):
        return self.__nac
    def get_moeda(self):
        return self.__moeda
    def get_populacao(self):
        return self.__populacao
    def get_capitalid(self):
        return self.__capitalid
    def get_cod(self):
        return self.__cod
    def to_dict(self):
        return {'ID' : self.__id, 'Nome' : self.__nome, 'Abreviação' : self.__abrev, 'Nacionalidade' : self.__nac, 'Moeda' : self.__moeda, 'População' : self.__populacao, 'ID da capital': self.__capitalid, 'Código de internet' : self.__cod}
    
#Persistência

class Paises (CRUD):
    @classmethod
    def salvar(cls):
        with open("paises.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("paises.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Pais(obj["_Pais__id"], obj["_Pais__nome"], obj["_Pais__abrev"], obj["_Pais__nac"], obj["_Pais__moeda"], obj["_Pais__populacao"], obj["_Pais__capitalid"], obj["_Pais__cod"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass