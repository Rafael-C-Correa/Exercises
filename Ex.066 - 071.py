from funex import cabecario

# Ex.066 - Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = cont = 0
cabecario('CONTADOR')
while True:
    num = float(input('Diga um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'''Total de números indicados: {cont}
Total da soma: {soma}''')

print('-----------------------------------------------------------------------------------')

# Ex.067 - Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

cabecario('TABUADA')
while True:
    s = int(input('Digite o número: '))
    if s > 0:
        c = 0
        print('-'*13)
        while c < 11:
            print(f'{s} * {c} = {s * c}')
            c += 1
        print('-'*13)
    else:
        break

print('-----------------------------------------------------------------------------------')

# Ex.068 - Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randrange
vit_j = vit_pc = 0
cabecario('PAR ou IMPAR')
while True:
    if vit_pc > 0:
        break
    else:
        escolha_pc = int(randrange(1, 11))
        escolha_j = int(input('Escolha um número: '))
        par_impar = int(input('PAR [1] ou IMPAR [2]? '))
        if par_impar == 1:
            if (escolha_j + escolha_pc) % 2 == 0:
                print(f'Sua escolha: {escolha_j} - Escolha pc: {escolha_pc}')
                print('VITÓRIA!')
                vit_j += 1
            elif (escolha_j + escolha_pc) % 2 != 0:
                print(f'Sua escolha: {escolha_j} - Escolha pc: {escolha_pc}')
                print('DERROTA!')
                vit_pc += 1
        elif par_impar == 2:
            if (escolha_j + escolha_pc) % 2 == 0:
                print(f'Sua escolha: {escolha_j} - Escolha pc: {escolha_pc}')
                print('DERROTA!')
                vit_pc += 1
            elif (escolha_j + escolha_pc) % 2 != 0:
                print(f'Sua escolha: {escolha_j} - Escolha pc: {escolha_pc}')
                print('VITÓRIA!')
                vit_j += 1
print(f'Total de vitórias consecutivas: {vit_j}')

print('-----------------------------------------------------------------------------------')

# Ex.069 -  Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior_18 = homens = mulher_20 = total_pessoas = 0
cabecario('CHECK PESSOAS')
while True:
    idade = int(input('\nIDADE: '))
    sexo = str(input('SEXO (M/F): ')).upper()
    total_pessoas += 1
    if sexo == 'M':
        homens += 1
    if idade > 18:
        maior_18 += 1
    if idade > 20 and sexo == 'F':
        mulher_20 += 1
    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('''
    CONTINUAR S/N? ''')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''
Total de Pessoas: {total_pessoas}
Total pessoas maiores de 18: {maior_18}
Total Homens: {homens}
Total Mulheres +20 anos: {mulher_20}''')

print('-----------------------------------------------------------------------------------')

# Ex.070 - Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total_gasto = mais_mil = mais_barato = cont = 0
nome_barato = ' '
cabecario('MERCADO DO ZÉ')
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Valor: '))
    cont += 1
    total_gasto += preco
    if preco > 1000:
        mais_mil += 1
    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        nome_barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('''
Continuar (S/N)? ''')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''
Total gasto na compra: R${total_gasto}
Total de produtos que custam +R$1000: R${mais_mil}
Nome do Produto mais Barato: {nome_barato} - Valor: R${mais_barato}''')

print('-----------------------------------------------------------------------------------')

# Ex.071 -  Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
# o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0
cabecario('RAFA BANK')
total_saque = int(input('Qual o valor a ser sacado? R$ '))
while True:
    while total_saque >= 50:
        cedulas_50 += 1
        total_saque -= 50
    while total_saque >= 20:
        cedulas_20 += 1
        total_saque -= 20
    while total_saque >= 10:
        cedulas_10 += 1
        total_saque -= 10
    while total_saque >= 1:
        cedulas_1 += 1
        total_saque -= 1
    break
print(f'''{'-'*25}
Total Cedulas de R$50: {cedulas_50}
Total Cedulas de R$20: {cedulas_20}
Total Cedulas de R$10: {cedulas_10}
Total Cedulas de R$1:  {cedulas_1}
{'-'*25}''')



