from funex import cabecario
from time import sleep
import pygame

# Ex.046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

for i in range (10, -1, -1):
    print(i)
    sleep(1)
print('BOOOOOOM!')
pygame.mixer.init()
pygame.mixer.music.load('fogos.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): pass

print('-----------------------------------------------------------------------------------')

# Ex.047 -  Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for i in range (0, 51, 2):
    print(i, end=" ")

print('-----------------------------------------------------------------------------------')

# Ex.048 - Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

s = 0
for c in range (501):
    if c % 3 == 0:
        print(c)
        s += c
print(f'A soma total dos números múltiplos de três é: {s}')

print('-----------------------------------------------------------------------------------')

# Ex.049 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

s = int(input('Diga o número: '))
for c in range(0,11):
    print(f'{s} * {c} = {s * c}')

print('-----------------------------------------------------------------------------------')

# Ex.050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

st = 0
for c in range(1,7):
    s = float(input(f'Diga o {c}º número: '))
    if s % 2 == 0:
        st += s
print(f'A soma total dos números é: {int(st)}')

print('-----------------------------------------------------------------------------------')

# Ex.051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

pt = float(input('PRIMEIRO TERMO: '))
r = float(input('RAZÃO: '))
for c in range(11):
    print(int(pt), end=" → ")
    pt += r
print('FIM')

print('-----------------------------------------------------------------------------------')

# Ex.052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('NÚMERO: '))
primo = 0
for c in range(2, (n)):
    if n % c == 0:
        primo += 1
if primo == 0:
    print(f'O número {n} é PRIMO')
else:
    print(f'O número {n} NÃO É PRIMO.')

print('-----------------------------------------------------------------------------------')

# Ex.053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('FRASE: ')).strip().upper().split()
junto = ''.join(frase)
par = ''
for c in range(len(junto) -1, -1, -1):
    par += junto[c]
cabecario(f'FRASE: {junto} - OPOSTO: {par}')
if junto == par:
    cabecario('É PALÍNDROMO')
else:
    cabecario('NÃO É PALINDROMO')

print('-----------------------------------------------------------------------------------')

# Ex.054 - Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quais pessoas ainda não atingiram a maioridade e quantas já são maiores.

maior_idade = []
menor_idade = []
for c in range(1,8):
    anos = int(input(f'Ano de nascimento {c}ª pessoa: '))
    if (2021 - anos) >= 18:
        maior_idade.append(anos)
    else:
        menor_idade.append(anos)
print(f'''MAIORES DE IDADE: {maior_idade}
MENORES DE IDADE: {menor_idade}''')

print('-----------------------------------------------------------------------------------')

# Ex.055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = []
n_pessoas = int(input('Quantas pessoas? '))
for c in range(1, n_pessoas+1):
    peso.append(int(input(f'Qual o peso da {c}ª pessoa? ')))
print(f'Pesos informados: {peso}')
print(f'''Menor peso: {min(peso)}Kg
Maior Peso: {max(peso)}Kg''')

print('-----------------------------------------------------------------------------------')

# Ex.056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

idade_media = 0
mais_velho = 0
nome_velho = ''
mulheres = []
soma_idade = 0
idade_mulheres = 0
for c in range(1, 5):
    cabecario(f'{c}ª PESSOA')
    nome = str(input(f'Nome: ')).upper()
    idade = int(input(f'Idade: '))
    sexo = str(input('Sexo: ')).upper()
    soma_idade += idade
    if idade > mais_velho and sexo == 'masculino'.upper():
        mais_velho = idade
        nome_velho = nome
    if idade <= 20 and sexo == 'feminino'.upper():
        mulheres.append(nome)
        idade_mulheres += 1
print(f'''Homem mais velho: {nome_velho} - Idade: {mais_velho}
Total de mulheres com menos de 20 anos: {idade_mulheres} - Nomes: {mulheres}
Media das idades: {soma_idade/4:.0f}''')

