"""
15. Faça uma função 'Troque', que recebe duas variáveis reais A e B e troca o valor delas (i.e., A recebe o valor de B e B recebe o valor de A).
"""

def change(value_A, value_B):
    aux = value_A
    value_A = value_B
    value_B = aux
    print(f'Os valores trocados são: {value_A} e {value_B}')

if __name__ == "__main__":
    try:
        value_A = float(input('Insira um valor: '))
        value_B = float(input('Insira outro valor: '))
        change(value_A, value_B)
    except:
        print('Insira um número real')


