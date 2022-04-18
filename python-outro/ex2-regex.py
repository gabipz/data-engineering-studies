# Verificar o tipo da variável sem mudá-la (usar regex)

import re

regex_string = re.compile(r'')
regex_int = re.compile(r'')
regex_float = re.compile(r'^(?!0\d)\d*(\.\d+)?$')
regex_boolean = re.compile(r'')

# ideia de resolução:
# 1) criar uma exp regular pra cada tipo de variavel
# 2) coloca-las em lista
# 3) varrer a procura de alguma correspondencia

# 3) usar filter list(filter(funcao, lista))

"essa variável é do tipo string mas deveria ser do tipo string"

"essa variavel é do tipo string mas deveria ser do tipo float"



#criar função que recebe um valor e printa qual é a variavel em regex.

#def check_char(var):



# Testes
