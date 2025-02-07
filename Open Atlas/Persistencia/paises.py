import json
from Persistencia.crud import CRUD
from Models.pais import Pais

class Paises (CRUD):
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