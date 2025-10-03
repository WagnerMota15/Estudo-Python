# Listas
n1 = [1, 2, 3, 4, 5]
n2 = [6, 7, 3, 9, 10]
valores = n1 + n2

print(valores)
print(type(valores))
print(valores[4])
print(valores[-2])

valores[4] = 50
print(valores[4])
print(f'Valores entre os indices 2 e 7: {valores[2:7]}')  # Slicing

print(f'Tamanho da lista: {len(valores)}')
print(f'Lista ordenada: {sorted(valores)}')
print(f'Lista invertida: {list(reversed(valores))}')
print(f'Soma dos elementos: {sum(valores)}')
print(f'Minimo elemento: {min(valores)}')
print(f'Maximo elemento: {max(valores)}')
print(f'Contagem do elemento 3: {valores.count(3)}')  # Quantas vezes o elemento aparece na lista

valores.append(14)  # Adiciona um elemento no final da lista
print(f'Lista após append: {valores}')
valores.pop()  # Remove o último elemento da lista
valores.pop(6)  # Remove o elemento na posição 6
valores.insert(3, 12)  # Adiciona o elemento 12 na posição 3
print(valores)
print(17 in valores)  # Verifica se o elemento 17 está na lista 

planetas = ['Mercurio', 'Venus', 'Terra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta)

# Exercício
bebibas_favoritas = []
for i in range(5):
    bebida = str(input(f'Informe a {i+1}ª bebida favorita: '))
    bebibas_favoritas.append(bebida)
bebibas_favoritas.sort()
print('\nBebidas escolhidas:')
for bebida in bebibas_favoritas:
    print(bebida)

# Tuplas -> listas imutáveis

# Funções matemáticas built-in e o módulo math
valores = [2,7,-3,4,9,12,-5]

print(f'Valor máximo: {max(valores)}')
print(f'Valor mínimo: {min(valores)}')
print(f'Soma dos valores: {sum(valores)}')
print(f'Valor absoluto de -5: {abs(-5)}')
print(f'Valor arredondado de 4.3: {round(4.3)}') # Arredonda para o inteiro mais próximo
print(f'Valor arredondado de 4.6: {round(4.6256, 2)}') # Arredonda para 2 casas decimais

print('\n---- Módulo Math ----\n')
import math

x = 8
y = 100

raiz = math.ceil(math.sqrt(x)) # Arredonda para cima
raiz2 = math.floor(math.sqrt(x)) # Arredonda para baixo
potencia = math.pow(x, 3)
logaritmo = math.log10(y)

print(f'Raiz quadrada de {x} (arredondada para cima): {raiz}')
print(f'Raiz quadrada de {x} (arredondada para baixo): {raiz2}')
print(f'{x} elevado à potência 3: {potencia}')
print(f'Logaritmo de {y} na base 10: {logaritmo}')
print(f'fatorial de x: {math.factorial(x)}')
print(f'{x/math.inf} (Divisão de x por infinito)')
print(f'Constante Pi: {math.pi}')
print(f'Constante e: {math.e}')
print(f'Valor do cosseno de 60 graus: {math.cos(math.radians(60))}') # Converte graus para radianos

# Manipulação de strings
nome = 'Wagner'
sobrenome = 'Mota'
nome_completo = nome + ' ' + sobrenome
print(f'Nome completo: {nome_completo}')
print('Mota' in nome_completo) 
split = nome_completo.split(' ') # Divide a string em uma lista
print(f'Split: {split}')
find = nome_completo.find('t') # Retorna o índice do início da substring
print(f'Find: {find}')

print(f'Nome em maiúsculo: {nome_completo.upper()}')
print(f'Nome em minúsculo: {nome_completo.lower()}')
print(f'Nome com a primeira letra maiúscula: {nome_completo.capitalize()}')
print(f'Nome com a primeira letra de cada palavra maiúscula: {nome_completo.title()}') 

nome_completo = nome_completo.replace('Mota', 'Sobrinho')
print(f'Nome completo após replace: {nome_completo}')
# strip, lstrip(à esquerda), rstrip(à direita) -> remove espaços 

print(nome_completo.startswith('Wag')) # Verifica se a string começa com a substring
print(nome_completo.endswith('nho')) # Verifica se a string termina com a

Docstring = """ Docstring é uma espécie de documentação que podemos inserir dentro de um módulo, função ou classe no Python. """
# Dicionários
elemento = {
    'nome': 'Hidrogênio',
    'símbolo': 'H',
    'número atômico': 1,
    'massa atômica': 1.008,
    'categoria': 'Não metal',
    'estado da matéria': 'Gás',
    'ponto de fusão (°C)': -259.16,
    'ponto de ebulição (°C)': -252.87,
    'densidade (g/cm³)': 0.00008988,
    'configuração eletrônica': '1s¹'
}
print(f'Elemento: {elemento["nome"]} ({elemento["símbolo"]})')
print(elemento.keys())
print(elemento.values())
for i in elemento.items():
    print(i)
elemento['período'] = 1
print(elemento)

del elemento['período']
print(elemento)

elemento.clear() # Limpa o dicionário
print(elemento)
del elemento # Deleta o dicionário

# Sets -> Conjuntos (não permitem elementos duplicados)
planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)
print('Ceres' in planeta_anao) 

for astro in planeta_anao:
    print(astro.upper())  

astros1 = {'Sol', 'Mercúrio', 'Vênus', 'Terra', 'Marte'}
astros2 = {'Júpiter', 'Saturno', 'Urano', 'Netuno', 'Terra', 'Marte'}
print(astros1.union(astros2))
print(astros1.intersection(astros2))
print(astros1.difference(astros2)) 
print(astros1.symmetric_difference(astros2))  # Elementos que estão em um ou outro conjunto, mas não em ambos
