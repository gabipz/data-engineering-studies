"""
Faça um algoritmo que receba um número inteiro positivo n e calcule:
(a) n!
(b) Somatório de 1 até n
Obs.: Crie uma função para cada letra.
"""

def factorial(number):
    fat = 1
    for i in range(number+1):
        if i <= 1:
            fat = 1
        else:
            fat *= i
    print(f'Fatorial de {number} = {fat}')


def sum_all(number):
    number_list = []
    for i in range(number):
        number_list.append(i+1)
    print(f'Somatório de 1 até {number} = {sum(number_list)}')

if __name__ == "__main__":
    number = int(input('Insira um número inteiro: '))
    factorial(number)
    sum_all(number)

