#Programa de adivinhação de um número(computador)
import random #importar a biblioteca random

numero_computador = random.randint(1,20)
numero_usuario = int()
tentativas = 0
while numero_computador != numero_usuario: #estrutura de repetição
    print('Digite um número entre 1 e 20:')
    numero_usuario = int(input()) #usuário digita o valor 
    tentativas += 1 #numero de tentativas do usuário
    
    #condicionais para verificar se o usuário adivinhou o número + dicas:
    if numero_usuario < numero_computador:
        print('Muito baixo.')
    elif numero_usuario > numero_computador:
        print('Muito alto.')
    elif numero_usuario == numero_computador:
        print(f'Você adivinhou o número {numero_computador} em {tentativas} tentativas.')
        