import turtle
from random import randint

turtle.tracer(0)  # programa para de atualizar a imagem do turtle toda hora
weeks = 0  # tempo de duração da simulação é contabilizado em semanas
turtle.bgcolor("black")  # muda a cor do plano de fundo de branco para preto
turtle.screensize(500, 350)  # limita tela na horizontal em 600 pixels e na vertical em 300


aggressiveness = int(input('De 1 a 10 o quão a chance do individuo ser infectado pelo virus')) #define a chance de ser infectado
mortality = int(input('De 0 a 1 o quão mortal é o virus?')) #define se o grau de mortalidade do virus
infection_rate = int(input('De 0 a 20 o quão grande é a area de infecção do virus?')) #aumenta a area de infecção do virus

person_id = {}  # Todas as pessoas não contaminadas da simulação estão contidas aqui
infected_id = {}  # Todas as pessoas contaminadas da simulação estão contidas aqui


healthy_people = [] # contagem da população saudavel
infected_people = [] # contagem da população infectada do dicionario infected_id
infected_people1 = [] #contagem da população infectada do dicionario person_id
immune_people = [] # população imune

def born_healthy_people(numero_de_pessoas):

    '''
    :param numero_de_pessoas: numeoro de pessoas saudaveis que você quer
    :return: bolinhas verdes simbolizando pessoas saudaveis
    '''


    for i in range(numero_de_pessoas):
        # criando as primeiras pessoas saudaveis
        person_id[i] = {}
        person_id[i]['people'] = turtle.Turtle()  # cria uma pessoa (representadas na simulação como uma esfera colorida
        person_id[i]['people'].shape('circle')  # o formato do turtle se torna um circulo
        person_id[i]['people'].color('green')  # A pessoa ganha a tonalidade acinzentada signifcando que está saudavel
        person_id[i]['people'].penup()  # limpa o rastro deixado pelo turtle
        person_id[i]['people'].setpos(randint(-570, 570), randint(-270, 270))  # com o auxilio da var radnit do modulo random a pessoa é posicionada em uma posição aleatoria
        person_id[i]['living_weeks_healthy'] = randint(0, 2300)  # tempo de vida
        person_id[i]['living_in_the_simulation'] = 0  # tempo que ela esta na simulção, contabilizado em semanas
        person_id[i]['living_infected'] = 0  # tempo que ela esta sendo infectada caso contraia a doença
        person_id[i]['situation'] = 3  # situação 3 significando estar saudavel
        healthy_people.append(person_id[i])  # a cada nascimento de uma pessoa adiciona um na contagem de pessoas saudaveis

def born_infected(numero_de_pessoas_infectadas):

    '''
    :param numero_de_pessoas_infectadas: numeoro de pessoas infectdas que você quer
    :return: bolinhas vermelhas simbolizando pessoas infectadas
    '''


    for i in range(numero_de_pessoas_infectadas):
        # criando as primeiras pessoas doentes
        infected_id[i] = {}
        infected_id[i]['people'] = turtle.Turtle()  # cria uma pessoa (representadas na simulação como uma esfera colorida
        infected_id[i]['people'].shape('circle')  # o formato do turtle se torna um circulo
        infected_id[i]['people'].color('red')  # A pessoa ganha a tonalidade acinzentada signifcando que está saudavel
        infected_id[i]['people'].penup()  # limpa o rastro deixado pelo turtle
        infected_id[i]['people'].setpos(randint(-570, 570), randint(-270, 270))  # com o auxilio da var radnit do modulo random a pessoa é posicionada em uma posição aleatoria
        infected_id[i]['living_weeks_infected'] = randint(0, 2350)  # tempo de vida
        infected_id[i]['living_in_the_simulation'] = 0  # tempo que ela esta na simulção, contabilizado em semanas
        infected_id[i]['situation'] = 2  # situação 2 significando estar infectada
        infected_people.append(infected_id[i]) # a cada nascimento de uma pessoa adiciona um na contagem de pessoas infectadas


born_healthy_people(140)
born_infected(10)


def move_population():

    '''
    :return: movimenta a população aleatoriamente
    '''

    for i in range(len(person_id)):
        person_id[i]['people'].rt(randint(0, 360))  # escolhe um angulação no intevalo de [0, 360] para comandar a pessoa ir na quela direçã0
        person_id[i]['people'].fd(randint(10, 15))  # determina o quão longe a pessoa vai andar na direção acima
    turtle.update()

    for index in range(len(infected_id)):
        infected_id[index]['people'].rt(randint(0, 360))  # escolhe um angulação no intevalo de [0, 360] para comandar a pessoa ir na quela direçã0
        infected_id[index]['people'].fd(randint(10, 15))  # determina o quão longe a pessoa vai anda na direção acima
    turtle.update()


def check_position():

    '''
    :return: verifica se a boliha está na faixa de tela escolhida
    '''

    for i in person_id: #checar no dicionario person_id
        cordx = person_id[i]['people'].xcor()  # cordenada horizontal da pessoa
        cordy = person_id[i]['people'].ycor()  # cordenada vertical da pessoa
        #caso alguma coordenada da bolinha esteja fora da tela definida ela é altomaticamente posicionada para borda dessa tela
        if cordx > 500:
            person_id[i]['people'].setx(500)
        elif cordy > 350:
            person_id[i]['people'].sety(350)
        elif cordx < -500:
            person_id[i]['people'].setx(-500)
        elif cordy < -350:
            person_id[i]['people'].sety(-350)

    for i in infected_id: #checar no dicionario infected_id
        cordx = infected_id[i]['people'].xcor()  # cordenada horizontal da pessoa
        cordy = infected_id[i]['people'].ycor()  # cordenada vertical da pessoa
        #caso alguma coordenada da bolinha esteja fora da tela definida ela é altomaticamente posicionada para borda dessa tela
        if cordx > 500:
            infected_id[i]['people'].setx(500)
        elif cordy > 350:
            infected_id[i]['people'].sety(350)
        elif cordx < -500:
            infected_id[i]['people'].setx(-500)
        elif cordy < -350:
            infected_id[i]['people'].sety(-350)


def infection(taxa_de_contaminação, range_inf):

    '''
    :param taxa_de_contaminação: de 0 a 10 o quão letal será o virus
    :param range_inf: aumento do raio de containação pelo usuario
    :return: uma pessoa infectada, se tornando uma bolinha vermelha
    '''


    for i1 in person_id:
        if person_id[i1]['situation'] == 3:
            for i2 in infected_id:
                if infected_id[i2]['situation'] == 2:
                    if i1 != i2:
                        cordAx = person_id[i1]['people'].xcor()  # cordenada horizontal da pessoa
                        cordAy = person_id[i1]['people'].ycor()  # cordenada vertical da pessoa
                        cordBx = infected_id[i2]['people'].xcor()  # coordenada horizontal de outra pessoa
                        cordBy = infected_id[i2]['people'].ycor()  # coodenada vertical de outra pessoa
                        if cordAx + (15+range_inf) >= cordBx - (15+range_inf) and cordAx - (15+range_inf) <= cordBx +(15+range_inf) and cordAy + (15+range_inf) >= cordBy - (15+range_inf) and cordAy - (15+range_inf) <= cordBy + (15+range_inf):  # definindo uma area de contaminação
                            chance_to_get_infected = int(randint(0, 10))  # definindo  a chance de contaminação
                            if chance_to_get_infected >= (10 - taxa_de_contaminação):
                                person_id[i1]['people'].color('red')
                                person_id[i1]['situation'] = 2 #o individuo entra na situação de infectado
                                person_id[i1]['living_infected'] = 0
                                if person_id[i1] in healthy_people:
                                    infected_people1.append(person_id[i1])
                                    healthy_people.remove(person_id[i1])


    for i1 in person_id:
        if person_id[i1]['situation'] == 3:
            for i2 in person_id:
                if person_id[i2]['situation'] == 2:
                    if i1 != i2:
                        cordAx = person_id[i1]['people'].xcor()  # cordenada horizontal da pessoa
                        cordAy = person_id[i1]['people'].ycor()  # cordenada vertical da pessoa
                        cordBx = person_id[i2]['people'].xcor()  # coordenada horizontal de outra pessoa
                        cordBy = person_id[i2]['people'].ycor()  # coodenada vertical de outra pessoa
                        if cordAx + (15+range_inf) >= cordBx - (15+range_inf) and cordAx - (15+range_inf) <= cordBx + (15+range_inf) and cordAy + (15+range_inf) >= cordBy - (15+range_inf) and cordAy - (15+range_inf) <= cordBy + (15+range_inf):  # definindo uma area de contaminação
                            chance_to_get_infected = int(randint(0, 10))  # definindo  a chance de contaminação
                            if chance_to_get_infected >= (10 - taxa_de_contaminação):
                                person_id[i1]['people'].color('red')
                                person_id[i1]['situation'] = 2 # o individuo entra na situação de infectado
                                person_id[i1]['living_infected'] = 0
                                infected_people1.append(person_id[i1])
                                if person_id[i1] in healthy_people:
                                    healthy_people.remove(person_id[i1])


def check_healthy():

    '''
    :return: analisa e muda a cor das pessoas saudaveis de acordo com seu tempo de vida
    '''


    for i in person_id:  # laço for para analisar as pessoas saudaveis
        person_id[i]['living_in_the_simulation'] += 1 #a cada loop aumenta uma semana de vida dentro da simulação
        person_id[i]['living_weeks_healthy'] += 1 #a cada loop aumenta uma semana de vida total

        if person_id[i]['living_in_the_simulation'] > 52 and person_id[i]['situation'] == 1:  # se uma pessoa é saudavel e esta assim a mais de 52 semanas ela perde sua imunidade
            person_id[i]['people'].color('green')  # a pessoa ganha a tonalidade esverdeada mostando que esta sucetivel a infecção
            person_id[i]['situation'] = 3  # é atribuido o valor 3 em situation que significa sucetivel a infecção

            if person_id[i] not in immune_people: # se a pessoa ainda não foi adicionada a lista de pessoas imunes ela sera
                immune_people.append(person_id[i])

                if person_id[i] in healthy_people: # e se ele ainda estiver na lista de pessoas saudaveis sera excluida
                    healthy_people.remove(person_id[i])



        if person_id[i]['situation'] == 2:  # se uma pessoa que era saudavel se tornou infectada sera iniciada uma contagem de semanas que ela ficou infectada
            person_id[i]['living_infected'] += 1

        if person_id[i]['living_infected'] > 100:  # se a pessoa esta a mais de x semans com a infecção, então ela é curada
            person_id[i]['people'].color('grey')  # volta a ter a tonalidade acinzentada (saudavel)
            person_id[i]['situation'] = 1  # é atribuido o valor 1 em situation que significa cura
            person_id[i]['living_in_the_simulation'] = 0

            if person_id[i] not in immune_people:
                immune_people.append(person_id[i])
                infected_people1.remove(person_id[i])


        if person_id[i][ 'living_weeks_healthy'] > 2400:  # se a idade da pessoa for maior que 2400 semanas(50 anos) ela morre
            person_id[i]['people'].ht()  # ela fica oculta na simulação
            person_id[i]['situation'] = 4  # é atribuido o valor 4 em situation que significa falecimento

            if person_id[i]['situation'] == 2:
                infected_people1.remove(person_id[i])

            elif person_id[i]['situation'] == 3:
                immune_people.remove(person_id[i])

            elif person_id[i]['situation'] == 1:
                healthy_people.remove(person_id[i])



def check_infected():

    '''
    :return: analisa e muda a cor das pessoas infectadas de acordo com seu tempo de vida
    '''

    for i in infected_id:

        infected_id[i]['living_weeks_infected'] += 1  # conta o tempo que a pessoa ta infectada
        infected_id[i]['living_in_the_simulation'] += 1  # conta o tempo que a pessoa ta na simulaçao

        if infected_id[i]['living_in_the_simulation'] > 100:  # infection_gap: #se a pessoa esta a mais de x semans com a infecção, então ela é curada
            infected_id[i]['people'].color('grey')  # volta a ter a tonalidade acinzentada (saudavel)
            infected_id[i]['situation'] = 5  # é atribuido o valor 5 em situation que significa cura
            if infected_id[i] in infected_people:
                infected_people.remove(infected_id[i])
                immune_people.append(infected_id[i])

        if infected_id[i]['living_weeks_infected'] > 2400:  # se a idade da pessoa for maior que 2400 semanas(50 anos) ela morre
            infected_id[i]['people'].ht()  # ela fica oculta na simulação
            infected_id[i]['situation'] = 4  # é atribuido o valor 4 em situation que significa falecimento
            if infected_id[i] in infected_people:
                infected_people.remove(infected_id[i])



def die_by_infection(chance_of_die_by_infection):

    '''
    :param chance_of_die_by_infection: define o grau de mortalidade o virus
    :return: a pesssoa infectda morta ou não
    '''

    for i in infected_id:
        if infected_id[i]['situation'] == 2:
            chance_to_die = randint(0, 100)
            if chance_to_die < chance_of_die_by_infection:
                infected_id[i]['people'].ht()  # ela fica oculta na simulação
                infected_id[i]['situation'] = 4  # é atribuido o valor 4 em situation que significa falecimento
                if infected_id[i] in infected_people:
                    infected_people.remove(infected_id[i])

    for i in person_id:
        if person_id[i]['situation'] == 2:
            chance_to_die = randint(0, 100)
            if chance_to_die < chance_of_die_by_infection:
                person_id[i]['people'].ht()  # ela fica oculta na simulação
                person_id[i]['situation'] = 4  # é atribuido o valor 4 em situation que significa falecimento
                if person_id[i] in infected_people1:
                    infected_people1.remove(person_id[i])
                elif person_id[i] in infected_people:
                    infected_people.remove(person_id[i])


w = 140  # variavel indexadora para manipular o nascimento de individuos semanalmente

while True:

    total_population = int(len(healthy_people)) + int(len(infected_people1)) + int(len(infected_people1)) + int(len(immune_people)) #população total é a soma do numero de individuos contidos em cada uma das listas

    move_population()
    infection(aggressiveness, infection_rate)
    die_by_infection(mortality)
    check_healthy()
    check_infected()
    check_position()

    # nascimento de uma pessoa saudavel
    if total_population < 300:  # total_population < 300:  # a cada semana, cada individuo saudavel tem 1% de chance de ter um filho
        chance_to_have_a_kid = int(randint(0, 10))

        if chance_to_have_a_kid >= (9):  # nascimento de uma pessoa saudavel
            # criando as primeiras pessoas saudaveis
            person_id[w] = {}
            person_id[w]['people'] = turtle.Turtle()  # cria uma pessoa (representadas na simulação como uma esfera colorida
            person_id[w]['people'].shape('circle')  # o formato do turtle se torna um circulo
            person_id[w]['people'].color('green')  # A pessoa ganha a tonalidade esverdeada signifcando que está saudavel
            person_id[w]['people'].penup()  # limpa o rastro deixado pelo turtle
            person_id[w]['people'].setpos(randint(-570, 570), randint(-270, 270))  # com o auxilio da var radnit do modulo random a pessoa é posicionada em uma posição aleatoria
            person_id[w]['living_weeks_healthy'] = 0  # tempo de vida
            person_id[w]['living_in_the_simulation'] = 0 #tempo de vida na simulação
            person_id[w]['living_infected'] = 0 #tempo que esta infectada
            person_id[w]['situation'] = 3
            healthy_people.append(person_id[w])  # a cada nascimento de uma pessoa adiciona um na contagem de pessoas saudaveis
            w += 1
    weeks += 1


    print(f'imune:{len(immune_people)}, saudavel:{len(healthy_people)}, infectados:{int(len(infected_people)) + int(len(infected_people1))}, semanas:{weeks}, população total:{total_population}')




turtle.mainloop()
