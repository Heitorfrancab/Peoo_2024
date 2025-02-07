class Usuario:
    def __init__(self, id, email, nome, senha):
        self.__id = id
        self.__email = email
        self.__nome = nome
        self.__senha = senha
    def get_id(self):
        return self.__id
    def get_email(self):
        return self.__email
    def get_nome(self):
        return self.__nome
    def get_senha(self):
        return self.__senha