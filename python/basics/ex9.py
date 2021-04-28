"""
Faça uma função que retorne o maior fator primo de um número.
"""
def highest_prime(number):
    
    primes = []
    for i in range(number):
        control = 0
        for j in range(number):
            if i%(j+1) == 0:
                control += 1
        if control == 2:
            primes.append(i)
    print(max(primes))

highest_prime(8) # 7
highest_prime(100) # 97

