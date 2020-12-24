import turtle

class Poulacao:
    def __init__(self, numero_de_pessoas, cor_do_grupo):
        self.__numero_de_pessoas = numero_de_pessoas
        self.__cor_do_grupo = cor_do_grupo
    
    def cria_individuo(self, numero_de_pessoas, cor_do_grupo):
        individuos = {}

        for i in range(numero_de_pessoas):
            individuos[i] = turtle.Turtle()
cara = Poulacao(50, 'azul')

cara.cria_individuo(50, 'azul')
