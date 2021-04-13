import os

s = os.environ['string']
f = os.environ['float']
i = os.environ['integer']
b = os.environ['boolean']

# Printar tipo das variaveis
#print(type(s), type(float(f)), type(int(i)), type(bool(b)))

# criar "if's" dizendo cada tipo de variavel
lista = [str(s), float(f), int(i), bool(b)]

for var in lista:
    if type(var) == str:
        print('A variavel eh uma string')
    elif type(var) == float:
        print('A variavel eh um decimal')
    elif type(var) == int:
        print('A variavel eh um inteiro')
    else:
        print('A variavel eh um booleano')

# sem if e com varias formas de fazer interpolacao de string
for var in lista:
    #print('A variavel eh do tipo:', type(var))
    #print('A variavel eh do tipo: ' + str(type(var)))
    #print('A variavel eh do tipo: {var_type}'.format(var_type=str(type(var))))
    print(f'A variavel eh do tipo: {str(type(var))}')
