# # Função print
# print('Imprime a mensagem e muda a linha')
# print('Imprime a mensagem sem mudar a linha', end = '')
# print(' Continuo na mesma linha!')

# nome = 'Maria'
# idade = 22
# print('O nome dela e {0} e ela tem {1} anos'.format(nome, idade))

# nome = 'João'
# idade = 30
# print(f'O nome dele e {nome} e ele tem {idade} anos')

# valor = 10.524298
# print(f'O valor e {valor:.2f}')  # Formata para 2 casas decimais

# nome = 'Wagner'
# idade = 20
# print(f'Nome:\t{nome}\tIdade:\t{idade}')  # \t adiciona tabulação

# # Estruturas de repetição
# num = 1
# while (num <= 10):
#     print(num)
#     num += 1  
# print('Acabou!')

# nome = None
# while True:
#     nome = input('Digite seu nome, ou x para parar: ')
#     if nome.lower() == 'x':
#         break
#     print(f'Seu nome é {nome}')

# lista = [1, 2, 3, 4, 5]
# palavra = 'Python\n'
# for letra in palavra:
#     print(letra)
# # range(valor_inicial, valor_final, incremento)
# for numero in range(1,11):
#     print(numero)

# nome = input('Digite seu nome: ')
# for x in range(10):
#     print(f'{nome}')

# for x in range(2,20,4):
#     print(x)

# pedras = ['Ametista', 'Citrino', 'Diamante', 'Esmeralda', 'Rubi', 'Safira']
# for pedra in pedras:
#     if pedra == 'Citrino':
#         continue
#     print(pedra)

# # Laços encadeados
# for x in range(1,6):
#     print(f'\nRodada: {x}')
#     for y in range(5, 0, -1):
#         print(f'valor: {y}')

import random
# for x in range(1,6):
#     print(f'\nConjunto {x}')
#     for y in range(5):
#         num = random.randint(1,100)
#         print(f'valor: {num}')

## modulos
import math # from math import sqrt, sin ; math as m
print(math.sqrt(25))

## aleatorios
valor = random.randint(1,50)
print(valor)

print('Gerar cinco numeros aleatorios entre 1 e 50: \n')
for i in range(5):
    print(random.randint(1,50))

num = random.random()
print(f'Numero gerado: {round(num * 10, 2)}')  ## Multiplica por 10 e arredonda até 2 casas decimais

valor = random.uniform(1,10)
print(f'Numero gerado: {round(valor, 2)}') 

L = [2,6,3,8,4,10,5]
n = random.choice(L)
print(f'Numero escolhido: {n}')

e = random.sample(L, 3)  ## Escolhe 3 numeros diferentes
print(f'Numeros extraidos: {e}')

print(f'Lista original: {L}')
random.shuffle(L)
print(f'Lista embaralhada: {L}')