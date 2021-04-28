"""
Escrever um programa que obtenha a data atual (ler dia, mês e ano) e exiba-a na tela no formato textual por extenso. A escrita da data por extenso deve ser realizada por um procedimento separado. Exemplo: Data: 01/01/2000, Imprimir: Sábado, 1 de janeiro de 2000.
"""
from datetime import date

weekdays = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
months = ('janeiro', 'fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')

current_date = date.today()
current_weekday = weekdays[current_date.weekday()]
text_date = '{}/{}/{}'.format(current_date.day, current_date.month, current_date.year)
day, month, year = text_date.split('/')

print(f'{current_weekday}, {day} de {months[int(month)-1]} de {year}.')

