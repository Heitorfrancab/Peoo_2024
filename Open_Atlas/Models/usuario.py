import json
from Models.crud import CRUD

#Modelo
class Usuario:
    def __init__(self, id, email, nome, senha):
        self.__id = id
        self.__email = email
        self.__nome = nome
        self.__senha = senha
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def get_email(self):
        return self.__email
    def get_nome(self):
        return self.__nome
    def get_senha(self):
        return self.__senha

#Persistência
class Usuarios (CRUD):
    @classmethod
    def salvar(cls):
        with open("usuarios.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("usuarios.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Usuario(obj["_Usuario__id"], obj["_Usuario__email"], obj["_Usuario__nome"], obj["_Usuario__senha"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass