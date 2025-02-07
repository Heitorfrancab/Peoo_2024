class Cidade:
    def __init__(self, id, nome, nat, populacao, idestado):
        self.__id = id
        self.__nome = nome
        self.__nat = nat
        self.__populacao = populacao
        self.__idestado = idestado
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