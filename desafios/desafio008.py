# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('========= CONVERSOR DE MEDIDAS =========')
medida = float(input('Coloque uma distância em metros: '))

cm = medida * 100
mm = medida * 1000

print(f'O valor em centímetros é igual a: {cm}')
print(f'O valor em milímetros é igual a: {mm}')