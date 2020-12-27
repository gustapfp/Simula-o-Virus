import turtle
from random import randint

população_infectada = []
população_imune = []
população_sucetivel_a_infeccao = []
class Poulacao:
    
    def __init__(self, numero_de_pessoas, grupo):
        self.__numero_de_pessoas = numero_de_pessoas
        self.__grupo = grupo

    
    def cria_individuo(self):
        '''
        cria os individuos de uma população
        numero_de_pessoas: numero de individuos a serem criados para essa população
        cor_do_grupo: Cor do grupo representa o estado de saude do individuo 
                    verde => susetivel a infecção
                    vermelho => infectado
                    cinza => imune
        '''
        print(self.__grupo)


        if self.__grupo is população_imune: # cinza
             cor_do_grupo = '#D3D3D3'            
        elif self.__grupo is população_infectada: # vermelha
            cor_do_grupo = '#FF0000'
        elif self.__grupo is população_sucetivel_a_infeccao: # verde
            cor_do_grupo = '#008000'
         
            
           
        print(cor_do_grupo)       
        
        for i in range(self.__numero_de_pessoas):
            numero_alearotio_paraY = randint(-400, 400)
            numero_alearotio_paraX = randint(-600, 600)
            self.__grupo.insert(i, turtle.Turtle())
            self.__grupo[i].shape('circle')
            self.__grupo[i].color(cor_do_grupo)
            self.__grupo[i].penup()
            self.__grupo[i].setx(numero_alearotio_paraX)
            self.__grupo[i].sety(numero_alearotio_paraY)
        return self.__grupo
    
    # def movimento_individuo(self):
    #     for i in range(self.__numero_de_pessoas):
    #         numero_alearotio = randint(-10, 10)
    #         individuos[i].forward(numero_alearotio)
class Simulação:

    def __init__(self, modulo):
        self.__modulo = modulo

    def tela_da_simulacao(self, tamanhox, tamanhoy, cor_da_tela):
        '''
        modulo: parametro para trazer o modulo turtle para dentro da função
        tamanhox: tamanho na vertical da tela da simulação
        tamanhoy: tamanha da horizontal do trla da simulação
        cor_da_tela: cor do fundo da tela da simulação
        '''

        self.__modulo.tracer(10) # Faz com que a tela seja atualizada toda hora
        self.__modulo.screensize(tamanhox, tamanhoy)
        self.__modulo.bgcolor((str(cor_da_tela)))

simulacao_virus = Simulação(turtle)
simulacao_virus.tela_da_simulacao(600, 400, 'black')

infectados = Poulacao(10, população_infectada)
sucetiveis_a_doença = Poulacao(140, população_sucetivel_a_infeccao)


weeks = 0
sucetiveis_a_doença.cria_individuo()
infectados.cria_individuo()

