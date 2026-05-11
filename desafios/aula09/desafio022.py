# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome completo com todas as letras maiúsculas e minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
nomeMaisculo = nome.upper()
nomeMinusculo = nome.lower()
tam = len(nome.replace(' ', ''))
nomeLista = nome.split(' ')
print(nomeLista)
primeiroNome = nomeLista[0]


print(f'Seu nome em maiúsculas é {nomeMaisculo}')
print(f'Seu nome em minúsculas é {nomeMinusculo}')
print(f'Seu nome tem ao todo {tam} letras')
print(f'Seu primeiro nome é {primeiroNome} e ele tem {len(primeiroNome)} letras')