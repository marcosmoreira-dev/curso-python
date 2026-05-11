# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a LARGURA da parede em metros: '))
altura = float(input('Digite a ALTURA da parede em metros: '))

area = largura * altura
quantidadeTinta = area / 2

print(f'A quantidade de tinta necessário é igual a: {quantidadeTinta}')
