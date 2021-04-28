"""
 12. Faça uma função que receba um número N e retorne a soma dos algarismos de N!. Ex: se N = 4, N! = 24. Logo, a soma de seus algarismos é 2 + 4= 6.
"""
def factorial(number):
    fac = 1
    for i in range(number+1):
        if i <= 1:
            fac = 1
        else:
            fac *= i
    return fac

def sum_digits(number):
    factorial_answer = factorial(number)
    split_number = [int(i) for i in str(factorial_answer)]
    return sum(split_number)

if __name__ == "__main__":
    try:
        number = int(input('Insira um número: '))
        print(sum_digits(number))
    except:
       print('Insira um número inteiro.')

