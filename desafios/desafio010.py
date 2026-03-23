# Crie um programa que leia o quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27

print('========= CONVERSOR CAMBIAL =========')

real = float(input('Digite o valor em R$: '))
dolar = real / 3.27

print(f'Você pode comprar US${dolar}')