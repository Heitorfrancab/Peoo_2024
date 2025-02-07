class Estado:
    def __init__(self, id, nome, abrev, nat, populacao, idpais):
        self.__id = id
        self.__nome = nome
        self.__abrev = abrev
        self.__nat = nat
        self.__populacao = populacao
        self.__idpais = idpais
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