from funex import cabecario
# Ex.028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange
n_ale = randrange(6)
n_adv = int(input('Qual número de 0 a 5 o PC escolheu? '))
if n_adv == n_ale:
    print('PARABÉNS! Você acertou!')
else:
    print(f'Você errou! O número escolhido foi: {n_ale}.')

print('-----------------------------------------------------------------------------------')

# Ex.029 - Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel_marcada = float(input('Qual foi a velocidade medida? '))
vel_limite = float(80.0)
valor_multa = (vel_marcada - vel_limite)*7
print(f'''
Velocidade limite: {vel_limite}km/h
Velicidade medida: {vel_marcada}km/h''')
if vel_marcada > vel_limite:
    print(f'''
Você ultrapassou o limite de velocidade! 
A multa será no valor de R$ {valor_multa}''')
else:
    print('''
Você estava dentro do limite.''')

print('-----------------------------------------------------------------------------------')

# Ex.0.30 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Diga um número: '))
if (n % 2) == 0:
    print('O número é PAR.')
else:
    print('O número é IMPAR.')

print('-----------------------------------------------------------------------------------')

# Ex.031 - Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

dist = float(input('Qual a distância da viagem? '))
if dist <= 200:
    valor = dist * 0.5
    print(f'O valor do seu voo será de: R${valor:.2f}.')
elif dist > 200:
    valor = dist * 0.45
    print(f'O valor de seu voo sera: R${valor:.2f}.')

print('-----------------------------------------------------------------------------------')

# Ex.032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Diga o ano que quer analisar: '))
if ano % 4 == 0:
    print(f'O ano {ano} É Bissexto.')
else:
    print(f'O ano {ano} NÃO é Bissexto.')

print('-----------------------------------------------------------------------------------')

# Ex.033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Diga o primeiro número: '))
b = int(input('Diga o segundo número: '))
c = int(input('Diga o terceiro número: '))
menor = a
if b<a and b<c:
    menor = b
elif c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
elif c>a and c>b:
    maior = c
print(f'Entre os números {a}, {b} e {c} o MAIOR é {maior} e o MENOR é {menor}.')

print('-----------------------------------------------------------------------------------')

# Ex.034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o seu salário? '))
reajuste_10 = (salario/100)*10
reajuste_15 = (salario/100)*15
if salario <= 1250:
    reajuste  = salario + ((salario/100)*15)
    print(f'''Salário ATUAL = R${salario}
Valor do REAJUSTE = R${reajuste_15}
Salário REAJUSTADO = R${reajuste}''')
else:
    reajuste = salario + ((salario/100)*10)
    print(f'''Salário ATUAL = R${salario}
Valor do REAJUSTE = R${reajuste_10}
Salário REAJUSTADO = R${reajuste}''')

print('-----------------------------------------------------------------------------------')

# Ex.035 -  Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

cabecario('VERIFICADOR DE TRIANGULOS')
la = float(input('Diga o primeiro lado: '))
lb = float(input('Diga o segundo lado: '))
lc = float(input('Diga o terceiro lado: '))
if la < (lb + lc) and lb < (la + lc) and lc < (la + lb):
    print(f'O lados {la, lb, lc} FORMAM um triangulo.')
else:
    print(f'Os lados {la, lb, lc} NÂO FORMAM um triangulo')