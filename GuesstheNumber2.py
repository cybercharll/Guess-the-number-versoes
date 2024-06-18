#Segunda versão do programa de adivinhação do número
import random #importar a biblioteca random

def adivinhe_numero():
    numero_computador = random.randint(1,10)
    numero_usuario = int()
    tentativas = 0
    while True:
        print('Digite um número entre 1 e 10:')
        numero_usuario = int(input())
        tentativas +=1
        
        if numero_usuario < numero_computador:
            print('Muito baixo.')
        elif numero_usuario > numero_computador:
            print('Muito alto.')
        elif numero_usuario == numero_computador:
            print(f'Você adivinhou o número em {tentativas} tentativas.')
            break

adivinhe_numero()
