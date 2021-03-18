# Ex.022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras no total (sem considerar os espaços)
# - Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ')
print(f'''Nome maiusculo: {nome.upper()}
Nome Minusculo: {nome.lower()}
O nome tem o total de {len(nome) - nome.count(' ')} letras
O primeiro nome tem um total de {nome.find(' ')} letras.''')
snome = nome.split()
print(f'O primeiro nome é: {snome[0]} e ele tem {len(snome[0])} letras')

print('-----------------------------------------------------------------------------------')

# Ex.023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = input('Diga um numero: ')
unidades = ['milhar', 'centena', 'dezena', 'unidade']
for i in range(len(numero) and len(unidades)):
    print(f'{unidades[i]} = {numero[i]}')

print('-----------------------------------------------------------------------------------')

# Ex.024 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Diga o nome da cidade: ').capitalize().split()
print(f'Há o nome Santos na cidade? {"Santos" in cidade}')

print('-----------------------------------------------------------------------------------')

# Ex.025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Diga o seu primeiro nome: ').capitalize()
print(f'Há Silva no nome? {"Silva" in nome}')

print('-----------------------------------------------------------------------------------')

# Ex.026 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = input('Diga o nome: ').upper()
print(f'''A letra - a - aparece {nome.count("A")} vezes.
A primeira ocorrência é na posição {nome.find("A") + 1}
A ultima ocorrência é na posição {nome.rfind("A") + 1}''')

print('-----------------------------------------------------------------------------------')

# Ex.027 - Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Diga o nome completo: ').upper()
n = nome.split()
print(f'''O nome completo é: {nome}
O primeiro nome é: {n[0]}
O ultimo nome é {n[-1]}''')