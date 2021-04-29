import turtle
from random import randint

populacao_infectada = []
populacao_imune = []
populacao_sucetivel_a_infeccao = []

controle_de_status_sucetivel = []
controle_de_status_infectado = []

class Populacao:
    def __init__(self, numero_de_pessoas, grupo, controla_status):
        self.__numero_de_pessoas = numero_de_pessoas
        self.grupo = grupo
        self.controla_status = controla_status

    def seleciona_cor(self):
        '''
        Seleciona a cor do indiviudo irá aparecer na simulaçao
                    verde => susetivel a infecção
                    vermelho => infectado
                    cinza => imune
        '''
        if self.grupo is populacao_imune: # cinza
             cor_do_grupo = 'grey'# '#D3D3D3'            
        elif self.grupo is populacao_infectada: # vermelha
            cor_do_grupo = 'red' # '#FF0000'
        elif self.grupo is populacao_sucetivel_a_infeccao: # verde
            cor_do_grupo ='green' # '#008000'   
        return cor_do_grupo

    def individuo(self, i):
        '''
        Retorna um individuo de uma grupo especifico, em um ponto aleatório 
        '''
        cor_individuo = self.seleciona_cor()
        numero_alearotio_paraY = randint(-385, 385)
        numero_alearotio_paraX = randint(-500, 500)
        self.grupo.insert(i, turtle.Turtle())
        self.grupo[i].shape('circle')
        self.grupo[i].color(cor_individuo)
        self.grupo[i].penup()
        self.grupo[i].setx(numero_alearotio_paraX)
        self.grupo[i].sety(numero_alearotio_paraY)
        self.controla_status.insert(i, {})
        self.controla_status[i]['dias_imune'] = 0
        self.controla_status[i]['dias_infectado'] = 0   
        


    def nasce_individuo(self, quantidade_de_pessoas_a_serem_criadas, tipo):
        '''
        cria os individuos de uma população
        quantidade_de_pessoas_a_serem_criadas: numero de individuos a serem criados para essa população
        '''
        cor_do_grupo = self.seleciona_cor()
        turtle.tracer(0)
        for i in range(quantidade_de_pessoas_a_serem_criadas):
            self.individuo(i)
        turtle.update()
        turtle.tracer(10)
        return self.__grupo, self.controla_status
    
    def movimenta_individuo(self):
        """
        Movimenta os individuos de forma aleatoria na simulação
        """


        numero_de_pessoas = int(len(self.__grupo))

        turtle.tracer(0)

        x = 0 
        while x < numero_de_pessoas:

            numero_aleatorio = randint(10, 15)
            angulo_selecionado = randint(0, 360)
            self.grupo[x].rt(angulo_selecionado)
            self.grupo[x].fd(numero_aleatorio)
            x += 1
        turtle.update()       
    
    def limita_bordas(self):
        """
        É predefinido uma area para simulação e impede que os individuos ultrapassem a borda da simulação
        """

        for i in range(len(self.__grupo)):
            if self.__grupo[i].xcor() > 500:
                self.__grupo[i].setx(500)
            elif self.__grupo[i].xcor() < -500:
                self.__grupo[i].setx(-500)
            elif self.__grupo[i].ycor() > 385:
                self.__grupo[i].sety(385)
            elif self.__grupo[i].ycor() < -385:
                self.__grupo[i].sety(-385)
            


class Simulacao:

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

if __name__ == "__main__":
    infectados = Populacao(10, populacao_infectada, controle_de_status_infectado)
    sucetiveis_a_doença = Populacao(190, populacao_sucetivel_a_infeccao, controle_de_status_sucetivel)

    simulacao_virus = Simulacao(turtle) # cria uma simulação no python
    simulacao_virus.tela_da_simulacao(600, 400, 'black') #seleciona as configurações da tela da simulação

    while True:
             

        weeks = 0
        sucetiveis_a_doença.nasce_individuo(190, 'sucetivel_a_doença')
        infectados.nasce_individuo(10, 'infectado')

