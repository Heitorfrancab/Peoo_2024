class Equacao():
    def __init__(self, a, b, c):
        self.__a  = int(a)
        self.__b  = int(b)
        self.__c  = int(c)
    def calc_delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    def TemRaizesReais(self):
        if self.calc_delta() < 0:
            return "Não há raiz real. "
        elif self.calc_delta() == 0:
            return "Há uma raiz real. "
        else:
            return "Há mais de uma raiz real. "
    def Raiz1(self):
        return (-self.__b + self.calc_delta() ** 2) / 2 * self.__a
    def Raiz2(self):
        return (-self.__b - self.calc_delta() ** 2) / 2 * self.__a
    def __str__(self):
        if self.calc_delta() < 0:
            return f"A equação {self.__a}x²+{self.__b}x+{self.__c} não tem raiz real."
        elif self.calc_delta() == 0:
            return f"A equação {self.__a}x²+{self.__b}x+{self.__c} tem uma raiz real: {self.Raiz1()}."
        else:
            return f"A equação {self.__a}x²+{self.__b}x+{self.__c} tem duas raizes reais: {self.Raiz1()} e {self.Raiz2()}."