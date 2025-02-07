import json
from Persistencia.crud import CRUD
from Models.estado import Estado

class estados (CRUD):
    objetos = []

    @classmethod
    def inserir(cls, obj):
        return super().inserir(obj)
    
    @classmethod
    def listar_id(cls, id):
        return super().listar_id(id)
    
    @classmethod
    def atualizar(cls, obj):
        return super().atualizar(obj)
    
    @classmethod
    def excluir(cls, obj):
        return super().excluir(obj)
    
    @classmethod
    def listar(cls):
        return super().listar()

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