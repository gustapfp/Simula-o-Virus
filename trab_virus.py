import turtle
from random import randint

populacao_infectada = []
populacao_imune = []
populacao_sucetivel_a_infeccao = []

class Poulacao:
    
    def __init__(self, numero_de_pessoas, grupo):
        self.__numero_de_pessoas = numero_de_pessoas
        self.__grupo = grupo

    def seleciona_cor(self):
        if self.__grupo is populacao_imune: # cinza
             cor_do_grupo = '#D3D3D3'            
        elif self.__grupo is populacao_infectada: # vermelha
            cor_do_grupo = '#FF0000'
        elif self.__grupo is populacao_sucetivel_a_infeccao: # verde
            cor_do_grupo = '#008000'   
        return cor_do_grupo
    
    def cria_individuo(self, quantidade_de_pessoas_a_serem_criadas):
        
        '''
        cria os individuos de uma população
        numero_de_pessoas: numero de individuos a serem criados para essa população
        cor_do_grupo: Cor do grupo representa o estado de saude do individuo 
                    verde => susetivel a infecção
                    vermelho => infectado
                    cinza => imune
        '''
    
        cor_do_grupo = self.seleciona_cor()
        turtle.tracer(0)
        for i in range(quantidade_de_pessoas_a_serem_criadas):
            numero_alearotio_paraY = randint(-385, 385)
            numero_alearotio_paraX = randint(-500, 500)
            self.__grupo.insert(i, turtle.Turtle())
            self.__grupo[i].shape('circle')
            self.__grupo[i].color(cor_do_grupo)
            self.__grupo[i].penup()
            self.__grupo[i].setx(numero_alearotio_paraX)
            self.__grupo[i].sety(numero_alearotio_paraY)
        turtle.update()
        turtle.tracer(10)
        return self.__grupo
    
    def limita_bordas(self):

        for i in range(len(self.__grupo)):
            if self.__grupo[i].xcor() > 500:
                self.__grupo[i].setx(500)
            elif self.__grupo[i].xcor() < -500:
                self.__grupo[i].setx(-500)
            elif self.__grupo[i].ycor() > 385:
                self.__grupo[i].sety(385)
            elif self.__grupo[i].ycor() < -385:
                self.__grupo[i].sety(-385)      
    
    def nasce_novo_individuo(self):
        '''
        A cada semana um individuo saudavel tem 10% chance de ter um novo filho
        '''
        populacao_saudavel = int(len(populacao_imune)) + int(len(populacao_sucetivel_a_infeccao))

        if populacao_saudavel < 300:
            chances_de_ter_um_filho = randint(0, 10)

            if chances_de_ter_um_filho > 9:
                index_do_novo_individuo = int(len(self.__grupo))                
                numero_alearotio_paraY = randint(-385, 385)
                numero_alearotio_paraX = randint(-500, 500)
                cor_do_grupo = self.seleciona_cor()
                self.__grupo.insert(index_do_novo_individuo, turtle.Turtle())
                self.__grupo[index_do_novo_individuo].shape('circle')
                self.__grupo[index_do_novo_individuo].color(cor_do_grupo)
                self.__grupo[index_do_novo_individuo].penup()
                self.__grupo[index_do_novo_individuo].setx(numero_alearotio_paraX)
                self.__grupo[index_do_novo_individuo].sety(numero_alearotio_paraY)

    def movimenta_individuo(self):

        turtle.tracer(0)
        for i in range(len(self.__grupo)):
            numero_aleatorio = randint(10, 15)
            angulo_selecionado = randint(0, 360)
            self.__grupo[i].rt(angulo_selecionado)
            self.__grupo[i].fd(numero_aleatorio)
        
        
        turtle.update()
        turtle.tracer(10)

def transmite_virus(taxa_de_cotantaminacao):
    for i in range(len(populacao_infectada)):
        infectado_intervalo_cordernada_x = (populacao_infectada[i].xcor() + 15)
        infectado_intervalo_cordenada_y = (populacao_infectada[i].ycor() + 15)
        for j in range(len(populacao_sucetivel_a_infeccao)):
            chance_de_ser_infectado = int(randint(0,10))
            sucetivel_intervalo_cordenada_x = (populacao_sucetivel_a_infeccao[j].xcor() + 15)
            sucetivel_intervalo_cordenada_y = (populacao_sucetivel_a_infeccao[j].ycor() + 15)
            if infectado_intervalo_cordernada_x + taxa_de_cotantaminacao >= sucetivel_intervalo_cordenada_x - taxa_de_cotantaminacao and infectado_intervalo_cordernada_x - taxa_de_cotantaminacao <= sucetivel_intervalo_cordenada_x + taxa_de_cotantaminacao and infectado_intervalo_cordenada_y + taxa_de_cotantaminacao >= sucetivel_intervalo_cordenada_y - taxa_de_cotantaminacao and infectado_intervalo_cordenada_y - taxa_de_cotantaminacao <=sucetivel_intervalo_cordenada_y + taxa_de_cotantaminacao:
                if chance_de_ser_infectado > 7:
                    print('infectado')
                    


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
    

simulacao_virus = Simulacao(turtle)
simulacao_virus.tela_da_simulacao(600, 400, 'black')

infectados = Poulacao(10, populacao_infectada)
sucetiveis_a_doença = Poulacao(190, populacao_sucetivel_a_infeccao)


weeks = 0
sucetiveis_a_doença.cria_individuo(190)
infectados.cria_individuo(10)

while weeks<100:
    sucetiveis_a_doença.movimenta_individuo()
    sucetiveis_a_doença.limita_bordas()
    sucetiveis_a_doença.nasce_novo_individuo()
    infectados.movimenta_individuo()
    infectados.limita_bordas()
    transmite_virus(20)
    weeks += 1
    #print(weeks)
    

