"""
Faça uma função que receba por parâmetro dois valores X e Z. Calcule e retorne o resultado de X^Z para o programa principal. Atenção não utilize nenhuma função pronta de exponenciação.
X --> base
Z --> exponent
"""

def exponential(base, exponent):
    result = 1
    for var in range(0,exponent):
        result *= base
    print(result)

# Teste
exponential(2,3) # 8
exponential(1,1) # 1
exponential(0,12) # 0
exponential(-8,4) # 4096


