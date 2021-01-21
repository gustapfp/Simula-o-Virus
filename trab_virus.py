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
        self.__grupo = grupo
        self.controla_status = controla_status
        
    # getter e setter precisam ser adicionados
    
    def seleciona_cor(self):
        '''
        Seleciona a cor do indiviudo irá aparecer na simulaçao
                    verde => susetivel a infecção
                    vermelho => infectado
                    cinza => imune
        '''
        if self.__grupo is populacao_imune: # cinza
             cor_do_grupo = 'grey'# '#D3D3D3'            
        elif self.__grupo is populacao_infectada: # vermelha
            cor_do_grupo = 'red' # '#FF0000'
        elif self.__grupo is populacao_sucetivel_a_infeccao: # verde
            cor_do_grupo ='green' # '#008000'   
        return cor_do_grupo
        
    #
    # def grupo_do_inviduo(self):
    #     return self.__grupo
    @property
    def grupo(self):
        return self.__grupo

    @grupo.setter 
    def grupo(self, grupo):
        self.__grupo = grupo
        
    def cria_individuo(self, quantidade_de_pessoas_a_serem_criadas, tipo):
        
        '''
        cria os individuos de uma população
        quantidade_de_pessoas_a_serem_criadas: numero de individuos a serem criados para essa população
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
            self.controla_status.insert(i, {})
            self.controla_status[i]['dias_imune'] = 0
            self.controla_status[i]['dias_infectado'] = 0

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
            

    def check_estado_do_individuo(self):

        for i in range(len(self.controla_status)):
            cor_do_individuo = self.__grupo[i].color()
            
            # SE PERDEU A IMUNIDADE

            if cor_do_individuo == ("grey", "grey"):  # se ele é cinza e esta imune
                self.controla_status[i]['dias_imune'] += 1 # aumenta um dia
                
            
            if self.controla_status[i]['dias_imune']  > 50 and  cor_do_individuo == ("grey", "grey"):  # se ele é cinza e ja passou do tempo de imunidade ele perde a imunidade e fica sucetivel a infecção
                self.controla_status[i]['dias_imune'] = 0 
                self.__grupo[i].color('green')     
                
            # SE FICOU CURADO DA DONEÇA

            if cor_do_individuo == ("red", "red"): 
                self.controla_status[i]['dias_infectado'] += 1
                # SE ELE MORREU INFECTADO
                chance_de_morrer_infectado = randint(0, 100)
                if chance_de_morrer_infectado > 99:
                    self.__grupo[i].ht()

            if self.controla_status[i]['dias_infectado']  > 50 and  cor_do_individuo == ("red", "red"):
                 self.controla_status[i]['dias_infectado'] = 0
                 self.__grupo[i].color('grey')

 
class Doentes(Populacao):
    def __init__(self, numero_de_pessoas, grupo, controla_status):
        super().__init__(numero_de_pessoas, grupo, controla_status)

    def transmite_virus(self, taxa_de_cotantaminacao):

        """
        individuos infectados podem infectar outros de pendendo da agressividade dele
        """

        numero_de_pessoas_sucetiveis_a_doença = int(len(populacao_sucetivel_a_infeccao)) # numero de pessoas que podem ser infectadas
        numero_de_pessoas_infectadas = int(len(populacao_infectada)) # numero de pessoas que estão infectadas
        i = 0 # variavel indexadora para comparar o numero de pessoas suceriveis a infecção
        x = 0

        while x < numero_de_pessoas_infectadas:

            if i <= numero_de_pessoas_infectadas: # enquanto a variavel i não ultrapassor os limites da numero de pessoas sucetiveis a infeção
                infectado_intervalo_cordernada_x = (populacao_infectada[i].xcor() + 15)
                infectado_intervalo_cordenada_y = (populacao_infectada[i].ycor() + 15)
                
            j = 0 #  variavel indexadora para usar no segundo loop

            while j < numero_de_pessoas_sucetiveis_a_doença: # verifica todos os elementos da lista e ve se um dos individuos infectados está encostando em um individuo sucetivel a infecção 
                
                chance_de_ser_infectado = int(randint(0,10))
                sucetivel_intervalo_cordenada_x = (populacao_sucetivel_a_infeccao[j].xcor() + 15)
                sucetivel_intervalo_cordenada_y = (populacao_sucetivel_a_infeccao[j].ycor() + 15)
                
                if infectado_intervalo_cordernada_x + taxa_de_cotantaminacao >= sucetivel_intervalo_cordenada_x - taxa_de_cotantaminacao and infectado_intervalo_cordernada_x - taxa_de_cotantaminacao <= sucetivel_intervalo_cordenada_x + taxa_de_cotantaminacao and infectado_intervalo_cordenada_y + taxa_de_cotantaminacao >= sucetivel_intervalo_cordenada_y - taxa_de_cotantaminacao and infectado_intervalo_cordenada_y - taxa_de_cotantaminacao <=sucetivel_intervalo_cordenada_y + taxa_de_cotantaminacao:
                    cor_transmisor_virus = populacao_infectada[i].color()
                    cor_receptor_virus = populacao_sucetivel_a_infeccao[j].color()
                    if chance_de_ser_infectado > 3 and cor_transmisor_virus == ("red", "red") and  cor_receptor_virus == ("green", "green"):
                        populacao_sucetivel_a_infeccao[j].color('red')    
                    # sprint(populacao_sucetivel_a_infeccao[j].color())                    
                j += 1
            i += 1    
            x += 1 

 

class SucetivelInfeccao(Populacao):

    def __init__(self, numero_de_pessoas, grupo, controla_status):
        super().__init__(numero_de_pessoas, grupo, controla_status)

    def nasce_novo_individuo(self):

        """
        A cada rodada um inividuo que não está doente tem a chance de ter um filho 
        """
        
        populacao_saudavel = int(len(populacao_imune)) + int(len(populacao_sucetivel_a_infeccao))

        if populacao_saudavel < 300:
            chances_de_ter_um_filho = randint(0, 10)
            if chances_de_ter_um_filho > 9:
                index_do_novo_individuo = int(len((super().grupo)))                
                numero_alearotio_paraY = randint(-385, 385)
                numero_alearotio_paraX = randint(-500, 500)
                cor_do_grupo = self.seleciona_cor()
                super().grupo.insert(index_do_novo_individuo, turtle.Turtle())
                super().grupo[index_do_novo_individuo].shape('circle')
                super().grupo[index_do_novo_individuo].color(cor_do_grupo)
                super().grupo[index_do_novo_individuo].penup()
                super().grupo[index_do_novo_individuo].setx(numero_alearotio_paraX)
                super().grupo[index_do_novo_individuo].sety(numero_alearotio_paraY)
                self.controla_status.insert(index_do_novo_individuo, {})
                self.controla_status[index_do_novo_individuo]['dias_imune'] = 0
                self.controla_status[index_do_novo_individuo]['dias_infectado'] = 0
            
    def se_esta_infectado_infecta_outros(self, taxa_de_cotantaminacao):
        numero_de_pessoas_sucetiveis_a_doença = int(len(populacao_sucetivel_a_infeccao)) # numero de pessoas que podem ser infectadas

        i = -1
        x = 0

        while x <= numero_de_pessoas_sucetiveis_a_doença:

            sucetivel_intervalo_cordenada_x1 = (populacao_sucetivel_a_infeccao[i].xcor() + 15)
            sucetivel_intervalo_cordenada_y1 = (populacao_sucetivel_a_infeccao[i].ycor() + 15)
                
            j = 0 #  variavel indexadora para usar no segundo loop

            while j < numero_de_pessoas_sucetiveis_a_doença: # verifica todos os elementos da lista e ve se um dos individuos infectados está encostando em um individuo sucetivel a infecção 
                
                chance_de_ser_infectado = int(randint(0,10))
                sucetivel_intervalo_cordenada_x2 = (populacao_sucetivel_a_infeccao[j].xcor() + 15)
                sucetivel_intervalo_cordenada_y2 = (populacao_sucetivel_a_infeccao[j].ycor() + 15)
                
                if sucetivel_intervalo_cordenada_x1 + taxa_de_cotantaminacao >= sucetivel_intervalo_cordenada_x2 - taxa_de_cotantaminacao and sucetivel_intervalo_cordenada_x1 - taxa_de_cotantaminacao <= sucetivel_intervalo_cordenada_x2 + taxa_de_cotantaminacao and sucetivel_intervalo_cordenada_y1 + taxa_de_cotantaminacao >= sucetivel_intervalo_cordenada_y2 - taxa_de_cotantaminacao and sucetivel_intervalo_cordenada_y1 - taxa_de_cotantaminacao <= sucetivel_intervalo_cordenada_y2 + taxa_de_cotantaminacao:
                    
                    cor_transmisor_virus = populacao_sucetivel_a_infeccao[i].color()
                    cor_receptor_virus = populacao_sucetivel_a_infeccao[j].color()
                    if chance_de_ser_infectado > 4 and  cor_receptor_virus == ("green", "green") and cor_transmisor_virus == ("red", "red"):
                       populacao_sucetivel_a_infeccao[j].color('red')                       
                j += 1
            x += 1 
        
        




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

infectados = Doentes(10, populacao_infectada, controle_de_status_infectado)
sucetiveis_a_doença = SucetivelInfeccao(190, populacao_sucetivel_a_infeccao, controle_de_status_sucetivel)

# 
weeks = 0
sucetiveis_a_doença.cria_individuo(190, 'sucetivel_a_doença')
infectados.cria_individuo(10, 'infectado')

while weeks<200:

    sucetiveis_a_doença.movimenta_individuo()
    sucetiveis_a_doença.limita_bordas()
    sucetiveis_a_doença.nasce_novo_individuo()
    sucetiveis_a_doença.se_esta_infectado_infecta_outros(20)
    sucetiveis_a_doença.check_estado_do_individuo()

    infectados.movimenta_individuo()
    infectados.limita_bordas()
    infectados.transmite_virus(20)
    infectados.check_estado_do_individuo()
    
    weeks += 1

   