# Ex.005 - Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite o número: '))
print(f'O antessessor é {n-1} o Número é {n} e o sucessor é {n+1}')

print('-----------------------------------------------------------------------------------')

# Ex.006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt
n = float(input('Digite o número: '))
print(f'O número é {n}, o dobro dele é {n*2}, o triplo dele é {n*3} e a raíz quadrada dele é {sqrt(n):.1f}')


print('-----------------------------------------------------------------------------------')

# Ex.007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

from statistics import median
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = [n1, n2]
print(f'A média entre a primeira nota ({n1}) e a segunda nota ({n2}) é: {median(m)}')

print('-----------------------------------------------------------------------------------')

# Ex.008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

distancia = float(input('Diga o valor da distância em metros: '))
print(f'A distancia de {int(distancia)}/m é igual à {int(distancia * 100)}/cm e {int(distancia * 1000)}/mm')

print('-----------------------------------------------------------------------------------')

# Ex.009 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número: '))
print(f'''{1} x {n} = {n*1}
{2} * {n} = {n*2}
{3} * {n} = {n*3}
{4} * {n} = {n*4}
{5} * {n} = {n*5}
{6} * {n} = {n*6}
{7} * {n} = {n*7}
{8} * {n} = {n*8}
{9} * {n} = {n*9}
{10} * {n} = {n*10}''')

print('-----------------------------------------------------------------------------------')

# Ex.010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira

# e mostre quantos dólares ela pode comprar.
reais = float(input('Quantos reais você tem? '))
print(f'Com os seus R${int(reais)}, você pode comprar U${reais * 5.43}')

print('-----------------------------------------------------------------------------------')

# Ex.011 - Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,sabendo que cada
# litro de tinta pinta uma área de 2 metros quadrados.

b = float(input('Qual o valor da base? '))
h = float(input('Qual o valor da altura? '))
a = (b * h)/2
print(f'''A tinta pinta 2 metros quadrados por litro. A área da sua parede é de: {float(a)} metros quadrados. 
São necessários {a/2} litros de tinta.''')

print('-----------------------------------------------------------------------------------')

# Ex.012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

v = float(input('Qual o valor do produto? (R$) '))
p = float(input('Qual o valor do desconto (%)? '))
vf = v * (1 - (p/100))
print(f'O valor do produto é R${v}, com desconto de {p}%, o valor final é de R${vf}.')

print('-----------------------------------------------------------------------------------')

# Ex.013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual o valor do salário? (R$) '))
p = float(input('Qual o valor do aumento? (%) '))
sf = s * (1 + (p/100))
print(f'O valor do salário é R${s}, com o aumento de {p}%, o salário novo será de R${sf:.1f}')

print('-----------------------------------------------------------------------------------')

# Ex.014 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

t = float(input('Digite o valor da temperatura (Cº): '))
print(f'A temperatura de {t}Cº corresponde a {(t * 1.8) + 32}Fº')

print('-----------------------------------------------------------------------------------')

# Ex.015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

diaria = float(input('Quantos dias alugados? '))
rodado = float(input('Quantos km rodados? '))
print(f'O valor total do aluguel é de {(diaria * 60) + (rodado * 0.15)}')
