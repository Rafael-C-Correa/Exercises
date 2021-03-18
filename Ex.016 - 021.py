import math
import random
import pygame

# Ex.016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
n = float(input('Diga um número: '))
print(f'A porção inteira de {n} é: {math.trunc(n)}')

print('-----------------------------------------------------------------------------------')

# Ex.017 - Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hip = math.hypot(co, ca)
print(f'Se o Cateto Op. é: {co} e o Cateto adj. é: {ca}, a Hipotenusa é igual a: {hip:.2f}')

print('-----------------------------------------------------------------------------------')

# Ex.018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo.
angulo = float(input('Diga o Ângulo: '))
rad = math.radians(angulo)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'O angulo é de {angulo}º. O Seno é de: {sen:.2f}, o Cosseno é de {cos:.2f} e a tangente é de: {tan:.2f}.')

print('-----------------------------------------------------------------------------------')

# Ex.019 -  Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
nomes = ['Rafael', 'Sabryna', 'Gabriel', 'João', 'Henrique']
print(f'A pessoa que limpará o quadro será: {random.choice(nomes)}.')

print('-----------------------------------------------------------------------------------')

# Ex.020 - O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
nomes = ['Rafael', 'Sabryna', 'Gabriel', 'João']
random.shuffle(nomes)
print(f'A ordem de apresentação sera:')
for i in range(len(nomes)):
    print(i, nomes[i])


print('-----------------------------------------------------------------------------------')

# Ex.021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
print('Tocar musica...')
pygame.mixer.init()
pygame.mixer.music.load('ff7.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): pass

