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