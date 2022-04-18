import os

s = os.environ['string']
f = os.environ['float']
i = os.environ['integer']
b = os.environ['boolean']

# 1- Criar um dicionário que devolve o nome da variável com nome legível
"""
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
"""

# 2 - Verificar o tipo da variável sem mudá-la (usar regex)

import re

regex_string = re.compile(r'')
regex_int = re.compile(r'')
regex_float = re.compile(r'/^(?!0\d)\d*(\\.\d+)?$/g')
regex_boolean = re.compile(r'/^True$|^False$/g')

dict_char = {
    regex_string : 'string',
    regex_int : 'inteiro',
    regex_float : 'decimal',
    regex_boolean : 'boleano'
}

def check_char(var):
    for match in dict_char.values():
        print(f'Essa variavel eh do tipo {type(var)}, mas deveria ser do tipo {var}')

# Testes
check_char('4.5')
check_char(b)
print(type(f))