"""
Crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medidas dos três lados de um triângulo. Elabore funções que:
- Determinar se eles lados formam um triângulo, sabendo que:
    • O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
- Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo. Sendo que:
	• Chama-se equilátero o triângulo que tem três lados iguais.
	• Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
	• Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

def which_triangle(side1, side2, side3):
    length_1_2 = side1 + side2
    length_1_3 = side1 + side3
    length_2_3 = side2 + side3
    if (side3 > length_1_2 or side2 > length_1_3 or side1 > length_2_3):
        print("Não é um triângulo!")
    elif (side1 == side2 and side2 == side3):
        print("O triângulo é equilatero.")
    elif (side1 != side2 and side2 != side3):
        print("O triângulo é escaleno.")
    else:
        print("O triângulo é isóceles.")

# Testes
which_triangle(20,15,100) # não é triangulo
which_triangle(4, 4, 4) # equilatero
which_triangle(8,8,4) # isoceles
which_triangle(16,20,30) # escaleno

     