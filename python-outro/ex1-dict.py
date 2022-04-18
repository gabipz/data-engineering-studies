# Criar um dicionário que devolve o nome da variável com nome legível

s = 'abc'
i = 10
f = 0.5
b = True

dict_char = {
    type(s) : 'string',
    type(i) : 'inteiro',
    type(f) : 'decimal',
    type(b) : 'boleano'
}

for var in dict_char.values():
    print(f'Variável do tipo: {var}')