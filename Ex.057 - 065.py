from funex import cabecario

# Ex.057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'M' and sexo != 'F':
    print('Opção inválida, tente novamente.')
    sexo = input(str('Diga o sexo (M/F): ')).upper()
print(f'Sexo informado: {sexo}')

print('-----------------------------------------------------------------------------------')

# Ex.058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randrange
n_ale = randrange(0, 11)
n_adv = int(input('Qual número de 0 a 10 o PC escolheu? '))
ten = 0
while n_adv != n_ale:
    n_adv = int(input('''Errado! 
Tente novamente: '''))
    ten += 1
cabecario(f'''PARABÉNS! Você acertou!
Número de tentativas: {ten}''')

print('-----------------------------------------------------------------------------------')

# Ex.059 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

x = int(input('Prmeiro número: '))
y = int(input('Segundo número: '))
esc = 0
while esc != 5:
    print('''
    CALCULADORA
    [1] SOMA
    [2] MULTIPLICAÇÃO
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR ''')
    esc = int(input('Escolha uma opção: '))
    if esc == 1:
        z = x + y
        cabecario(f'{x} + {y} = {z}')
        esc = int(input('''Escolha uma opção: '''))
    elif esc == 2:
        z = x * y
        cabecario(f'{x} * {y} = {z}')
        esc = int(input('Escolha uma opção: '))
    elif esc == 3:
        if x > y:
            cabecario(f'O número {x} é maior.')
        elif y > x:
            cabecario(f'O número {y} é maior')
        elif x == y:
            cabecario(f'Os números {x} e {y} são Iguais.')
        esc = int(input('Escolha uma opção: '))
    elif esc == 4:
        print('')
        x = int(input('Prmeiro número: '))
        y = int(input('Segundo número: '))
        esc = int(input('Escolha uma opção: '))
    else:
        if esc != 5:
            print('Alternativa inválida.')
cabecario('OBRIGADO')

print('-----------------------------------------------------------------------------------')

# Ex.060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:  5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número: '))
f = int(n)
nf = 1
print(f'{n}! = ', end='')
while f > 0:
    nf = nf * f
    print(f'{f} ', end=(''))
    print('* ' if f > 1 else "= ", end='')
    f -= 1
print(nf)

print('-----------------------------------------------------------------------------------')

# Ex.061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

pt = float(input('PRIMEIRO TERMO: '))
r = float(input('RAZÃO: '))
p = 0
while p < pt:
    print(f' {int(pt)} {"→" if p < 9 else ""}', end='')
    pt += r
    p += 1
    print('PAUSA')

print('-----------------------------------------------------------------------------------')

# Ex.062 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

cabecario('GERADOR DE PA')
pt = float(input('PRIMEIRO TERMO: '))
r = float(input('RAZÃO: '))
termo = pt
cont = 0
total = 0
mais = int(input('TERMOS: '))
total_pa = 0
while mais != 0:
    total += mais
    while cont < total:
        print(f' {int(pt)} {"→" if cont < total else ""}', end='')
        pt += r
        total_pa += pt
        cont += 1
        print(' PAUSA' if cont == total else '', end='')
    mais = int(input('\nQuantos mais deseja calcular: '))
print(f'''FIM
Total dos valores somados: {int(total_pa)}
Número de termos contados: {total}''')

# Ex.063 - Escreva um programa que leia um número N inteiro qualquer
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

primeiro_t = 0
segundo_t = 1
cont = 2
cabecario('SEQUENCIA DE FIBONACCI')
num_vez = int(input('Quantos deseja calcular? '))
print(f'{primeiro_t} → {segundo_t} → ', end='')
while cont < num_vez:
    terceiro_t = int(primeiro_t + segundo_t)
    cont += 1
    print(f'{terceiro_t} {"→ " if cont < num_vez else ""}', end='')
    primeiro_t = segundo_t
    segundo_t = terceiro_t

print('-----------------------------------------------------------------------------------')

# Ex.064 - Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n_input = 0
n_parada = 0
cont = 0
cabecario('CONTADOR')
while n_parada != 999:
    n_parada = int(input('Diga um número: '))
    if n_parada != 999:
        n_input += n_parada
        cont += 1
print(f'''FIM
TOTAL de números digitados: {cont}
SOMA dos números digitados: {n_input}''')

print('-----------------------------------------------------------------------------------')

# Ex.065 - Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

from math import inf
cabecario('CONTADOR')
resposta = 'S'.upper()
cont = 0
maior_n = 0
menor_n = inf
media = 0
while resposta == 'S':
    num = int(input('Digite um número: '))
    cont += 1
    media += num
    if cont > maior_n:
        maior_n = cont
    if menor_n > cont:
        menor_n = cont
    resposta = str(input('Deseja adicionar novamente (S/N)? ')).upper()
print(f'''Total de números: {cont}
Maior número: {maior_n}
Menor número: {menor_n}
Média: {media/cont}:.2f''')
