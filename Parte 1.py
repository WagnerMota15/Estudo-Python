nome = 'Wagner'
print("Ola, " + nome)
media = 0 
nota = 8.5
nome, idade = 'Wagner', 20
estado = True

# Função type() => mostra o tipo da variável
print("\n\nTipos das variaveis:")
print(type(media))
print(type(nota))
print(type(nome))
print(type(idade))
print(type(estado))
print(type(1 + 2j))  # Tipo complexo

# Função isinstance() => verifica se a variável é do tipo especificado
print("\n\nVerificações com isinstance():")
print(isinstance(nome, (int, bool))) # Verifica se é int ou bool
print(isinstance(idade, (int, float)))  # Verifica se é int ou float

a = 10
b = 5
c = 16
# Operações Aritméticas
print("\n\nOperacoes aritmeticas:")
print(a + b + c)
print(a - b)
print(a * c)  
print(c / b) 
print(a // b)
print(c % b)
print(a ** 7)

x = int(input("\n\nDigite um numero: "))
y = int(input("Digite outro numero: "))
print("Soma dos dois valores e: ", x + y)


# Operadores de comparação
x = y = z = False
n1 = n2 = 0

print("\n\nDigite um numero: ")
n1 = int(input())
n2 = int(input('Digite outro numero: '))
x = n1 == n2
print("n1 é igual a n2? ", x)

y = n1 != n2
print("n1 é diferente de n2? " + str(y)) # Concatenação de string, convertendo bool em str

# Operadores lógicos
idade = 20
altura = 1.68

resultado = idade >= 18 and altura >= 1.70
print("\n\nPode tirar a carteira de motorista? " +  str(resultado))

porta = 't'
janela = 'f'

alarme = porta == 't' or janela == 't'
print("\nO alarme vai disparar? " + str(alarme))

tem_dinheiro = False
print("\nRecebeu um pix!")
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)

# Condicionais
n1 = n2 = 0.0
media = 0.0

n1 = float(input("\n\nDigite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

if (media >= 7):
    print("Aprovado! Nota:")
elif (media >= 5 and media < 7):
    print("Recuperação!")
else:
    print("Reprovado!")

print("Média: ", media)