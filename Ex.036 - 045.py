from funex import cabecario

# Ex.036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

cabecario('CALCULADORA DE IMPRESTIMOS')
salario = float(input('Qual o seu salário? R$ '))
vimovel = float(input('Qual o valor do imóvel? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
meses = int(anos*12)
valor_parcela = vimovel/meses
print(f'''Valor do Imóvel: R${vimovel}
Numero de parcelas: {meses}
Valor das parcelas: R${valor_parcela:.2f}''')
if valor_parcela > (salario/100)*30:
    cabecario('IMPRESTIMO NÃO APROVADO')
else:
    cabecario('IMPRESTIMO APROVADO')

print('-----------------------------------------------------------------------------------')

# Ex.037 - Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

cabecario('CONVERSOR DE BASES NUMÉRICAS')
escolha = int(input('''[1] - BINÁRIO
[2] - OCTAL
[3] - HEXADECIMAL
Digite a opção desejada: '''))
numero = int(input('Escolha um número: '))
if escolha == 1:
    print(f'Número escolhido: {numero} - Binário: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'Número escolhido: {numero} - Octal: {oct(numero)[2:]}')
elif escolha == 3:
    print(f'Número escolhido: {numero} - Hexadecimal: {hex(numero)[2:]}')

print('-----------------------------------------------------------------------------------')

# Ex.038 - Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
maior = x
menor = y
if y < x:
    menor = y
    maior = x
elif x < y:
    menor = x
    maior = y
if x != y:
    print(f'O maior número é: {maior} e o menor número é: {menor}')
elif x == y:
    print(f'Os números {x} e {y} são iguais.')

print('-----------------------------------------------------------------------------------')

# Ex.039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
cabecario('CADASTRO ALISTAMENTO MILITAR')
ano_atual = date.today().year
ano_nascimento = int(input('Qual o ano de seu nascimento? '))
idade = (ano_atual - ano_nascimento)
print(f'Atualmente você tem {idade} anos de idade.')
if idade >= 18:
    print(f'APTO AO ALISTAMENTO MILITAR')
elif idade < 18:
    idade_restante = (18 - idade)
    ano_alistamento = (ano_atual + idade_restante)
    print(f'''INAPTO AO ALISTAMENTO MILITAR
Ano de alistamento: {ano_alistamento}
Período restante: {idade_restante}''')

print('-----------------------------------------------------------------------------------')

# Ex.040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

cabecario('MEDIA DE NOTAS')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
if media < 5.0:
    print(f'Média: {media:.2f} - REPROVADO')
elif media == 5.0 or media <= 6.9:
    print(f'Media: {media:.2f} - RECUPERAÇÃO')
elif media >= 7.0:
    print(f'Media: {media:.2f} - APROVADO')

print('-----------------------------------------------------------------------------------')

# Ex.041 - Programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
nascimento = int(input('Qual o ano de nascimento? '))
a_atual = date.today().year
idade_nat = (a_atual - nascimento)
mirim = range(0, 10)
infatil = range(10, 15)
junior = range(15, 20)
senior = range(20, 25)
if idade_nat in mirim:
    print(f'Idade: {idade_nat} - Mirin')
elif idade_nat in infatil:
    print(f'Idade: {idade_nat} - Infantil')
elif idade_nat in junior:
    print(f'Idade: {idade_nat} - Junior')
elif idade_nat in senior:
    print(f'Idade: {idade_nat} - Senior')
else:
    print(f'Idade: {idade_nat} - Master')

print('-----------------------------------------------------------------------------------')

# Ex. 042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

cabecario('VERIFICADOR DE TRIANGULOS')
la = float(input('Diga o primeiro lado: '))
lb = float(input('Diga o segundo lado: '))
lc = float(input('Diga o terceiro lado: '))
if la < (lb + lc) and lb < (la + lc) and lc < (la + lb):
    print(f'O lados {la, lb, lc} FORMAM um triangulo.')
    if la == lb and la == lc:
        print(f'O Triango de lados {la, lb, lc} é Equilátero')
    elif la == lb or la == lc or lb == lc:
        print(f'O Triango de lados {la, lb, lc} é Isósceles')
    else:
        print(f'O Triango de lados {la, lb, lc} é Escaleno')
else:
    print(f'Os lados {la, lb, lc} NÂO FORMAM um triangulo')

print('-----------------------------------------------------------------------------------')

# Ex.043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

cabecario('CALCULADORA DE IMC')
peso = float(input('Informe o peso (Kg): '))
altura = float(input('Informe a altura (m): '))
imc = peso/(altura**2)
if imc < 18.5:
    print(f'Peso: {peso}kg - IMC {imc:.0f} - Abaixo do Peso')
elif imc <= 25:
    print(f'Peso: {peso}kg - IMC {imc:.0f} - Peso Ideal')
elif imc <= 30:
    print(f'Peso: {peso}kg - IMC {imc:.0f} - Sobrepeso')
elif imc <= 40:
    print(f'Peso: {peso}kg - IMC {imc:.0f} - Obesidade')
elif imc > 40:
    print(f'Peso: {peso} - Obesidade Morbida')

print('-----------------------------------------------------------------------------------')

# Ex.044 -  Calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Digite o valor do produto: R$ '))
cabecario('Métodos de pagamento:')
escolha = int(input(f'''[1] À Vista dinheiro/cheque;
[2] À Vista no cartão;
[3] Até 2x no cartão;
[4] 3x ou mais no cartão.
Escolha uma opção: '''))
if escolha == 1:
    print(f'''Valor original: R${valor_produto}
Valor final (desconto de 10%): R${valor_produto - (valor_produto*0.1)}''')
elif escolha == 2:
    print(f'''Valor original: R${valor_produto}
Valor final (desconto de 5%): R${valor_produto - (valor_produto*0.05)}''')
elif escolha == 3:
    opcao_parcela = int(input('Deseja parcelar em 1 ou 2 vezes? '))
    if opcao_parcela == 1:
        print(f'Valor a ser pago: R${valor_produto}')
    elif opcao_parcela == 2:
        print(f'''Valor do produto: R${valor_produto} 
Valor da parcela: 2x de R${valor_produto/2}''')
elif escolha == 4:
    produto_juros = valor_produto + (valor_produto*0.2)
    opcao_parcela = int(input('Em quantas vezes deseja pagar? '))
    print(f'''Valor do produto: R${valor_produto}
Valor final (Juros de 20%): R${produto_juros} 
Valor da parcela: {opcao_parcela}x de R${produto_juros/opcao_parcela}''')

print('-----------------------------------------------------------------------------------')

# Ex.045 - Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep
ped = 'PEDRA'
pap = 'PAPEL'
tes = 'TESOURA'
pc_escolha = choice([ped, pap, tes])
cabecario('JOKENPO')
jog_escolha = int(input(f'''[1] - Pedra
[2] - Papel
[3] - Tesoura
Sua jogada: '''))
if jog_escolha == 1:
    jog_escolha = ped
elif jog_escolha == 2:
    jog_escolha = pap
elif jog_escolha == 3:
    jog_escolha = tes
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(0.5)
print(f'''{'=-' * 12}
Você Escolheu: {jog_escolha}
O PC Escohlheu: {pc_escolha}
{'=-' * 12}''')
if (jog_escolha == ped and pc_escolha == pap) or (jog_escolha == pap and pc_escolha == tes) or (jog_escolha == tes and pc_escolha == ped):
    print('VOCÊ PERDEU!')
elif (pc_escolha == ped and jog_escolha == pap) or (pc_escolha == pap and jog_escolha == tes) or (pc_escolha == tes and jog_escolha == ped):
    print('VOCÊ VENCEU!')
elif pc_escolha == jog_escolha:
    print('EMPATE')