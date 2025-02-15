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
    def __dict__(self):
        {'ID' : self.__id, 'Email' : self.__email, 'Nome' : self.__nome}
    def to_json(self):
        return {
            "id": self.get_id(),
            "email": self.get_email(),
            "nome": self.get_nome(),
            "senha": self.get_senha(),
        }
    
#Persistência
class Usuarios (CRUD):
    @classmethod
    def salvar(cls):
        with open("usuarios.json", mode="w") as arquivo:   # w - write
            json.dump([obj.to_json() for obj in cls.objetos], arquivo, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("usuarios.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Usuario(obj["id"], obj["email"], obj["nome"], obj["senha"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass