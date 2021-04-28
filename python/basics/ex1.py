"""
Crie um programa que leia três números. Para cada número, imprima o dobro. Use uma função que recebe como parâmetro um número inteiro e devolve o seu dobro. O valor calculado deve ser impresso na função principal.
"""
def double(number):
    print(f'Seu dobro é {2*number}.')

try:
    for i in range(3):
        number = int(input(f'Insira o {i+1}o número: '))
        double(number)
except:
    print("Insira um número inteiro.")

