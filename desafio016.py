"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
Ex: Digite um número: 6.127, o número 6.127 tem parte inteira 6"""

"""Floor serve para arrendar um numero, se digitar 9.123, com o floor fica 9"""

from math import floor
num = float(input("Digite um número: "))
print('O valor inteiro é {}'.format(floor(num)))