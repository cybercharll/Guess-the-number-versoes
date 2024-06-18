#Computador adivinha o número do usuário
import random

def computador_adivinha(x): #função principal do programa
    valor_baixo = 1 #por onde começa 
    valor_alto = x #onde termina a contagem
    feedback = '' #número que o usuário pensou
    while feedback != 'c': #loop principal não para enquanto a tentativa do computador não for igual ao do usuário
        if valor_baixo != valor_alto:
             tentativa_comp = random.randint(valor_baixo,valor_alto)
        else:
            tentativa_comp = valor_alto #valor_alto = valor_baixo 
        #variável para o usuário dizer se o computador acertou 
        feedback = input(f'Pensou em {tentativa_comp}? Digite (B) se for baixo, (A) se for alto, ou (C) se for correto:').lower()
        if feedback == 'a':
            valor_alto = tentativa_comp -1 #elimina uma porcentagem de valores que não podem ser o valor correto
        elif feedback == 'b':
            valor_baixo = tentativa_comp + 1 #elimina porcentagem de valores baixos deixando assim valores com maior probabilidade de acerto
    print(f'Eba! O computador adivinhou o seu número ({tentativa_comp})')

computador_adivinha(10)