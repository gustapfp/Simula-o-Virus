import turtle
from random import randint

class Poulacao:
    def __init__(self, numero_de_pessoas, cor_do_grupo):
        self.__numero_de_pessoas = numero_de_pessoas
        self.__cor_do_grupo = cor_do_grupo
    
    def cria_individuo(self, numero_de_pessoas, cor_do_grupo):
        '''
        cria os individuos de uma população
        numero_de_pessoas: numero de individuos a serem criados para essa população
        cor_do_grupo: Cor do grupo representa o estado de saude do individuo 
                    verde => susetivel a infecção
                    vermelho => infectado
                    cinza => imune
        '''
        individuos = {}

        for i in range(numero_de_pessoas):
            numero_alearotio_paraY = randint(-400, 400)
            numero_alearotio_paraX = randint(-600, 600)
            individuos[i] = turtle.Turtle()
            individuos[i].shape('circle')
            individuos[i].color(cor_do_grupo)
            individuos[i].penup()
            individuos[i].setx(numero_alearotio_paraX)
            individuos[i].sety(numero_alearotio_paraY)
    
def tela_da_simulacao(modulo, tamanhox, tamanhoy, cor_da_tela):
    '''
    modulo: parametro para trazer o modulo turtle para dentro da função
    tamanhox: tamanho na vertical da tela da simulação
    tamanhoy: tamanha da horizontal do trla da simulação
    cor_da_tela: cor do fundo da tela da simulação
    '''

    modulo.tracer(10) # Faz com que a tela seja atualizada toda hora
    modulo.screensize(tamanhox, tamanhoy)
    modulo.bgcolor(cor_da_tela)

tela_da_simulacao(turtle, 600, 400, 'black')
cara = Poulacao(50, 'azul')

cara.cria_individuo(50, 'blue')
    
