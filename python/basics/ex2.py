"""
Faça um programa receba dois números e execute as seguintes funções:
- Verificar se o número digitado é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo, O se negativo ou -1 se for igual a 0. Obedeça ao protótipo da função: int verifica(int num).
- Receber dois números inteiros positivos por parâmetro e retorne a soma dos N números inteiros existentes entre eles. int soma_entre(int num1, int num2).
"""

def check_positive_negative_number(number):
    if number > 0:
        return 1
    elif number < 0:
        return 0
    else:
        return -1

def sum_between(number1, number2):
    number_list = []

    difference = number2 - number1
    checked = check_positive_negative_number(difference)
    if checked == 0:
        difference = -difference
        aux = number1
        number1 = number2
        number2 = aux
        checked = 1
    if checked == 1:
        aux = difference
        while len(number_list) <= difference:           
            new_number = number2 - aux
            number_list.append(new_number)
            aux = aux - 1
        sum_list = sum(number_list)
        print(sum_list)
    else:
        print(number1+number2)


# Testes
sum_between(1,5) # 1+2+3+4+5 = 15
sum_between(4,1) # 1+2+3+4 = 10
sum_between(1,2) # 1+2 = 3
sum_between(1,1) # 1+1 = 2
sum_between(0,0) # 0+0 = 0
sum_between(0,5) # 0+1+2+3+4+5 = 15
sum_between(-1,2) # -1+0+1+2 = 2
sum_between(1,-2) # -2-1+0+1 = -2

