"""
Foi realizada um pesquisa de algumas características físicas de cinco habitantes de certa região. De cada habitante
foram coletados os seguintes dados: sexo, cor dos olhos (A Azuis ou C - Castanhos), cor dos cabelos (L - Louros,
P- Pretos ou C Castanhos) e idade. Faça uma função que leia esses dados em um vetor. Determine, por meio de outra
função a média de idade das pessoas com olhos castanhos e cabelos pretos. Mostre esse resultado no programa principal.
• Faça uma função que determine e devolva ao programa principal a maior idade entre os habitantes.
• Faça uma função que determine e devolva ao programa principal a quantidade de indivíduos do sexo feminino cuja idade
está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros.
"""
import pandas as pd

def input_data():
    print('------Preencha as informações da seguinte maneira------')
    print('- Gênero: M - masculino) ou F - feminino ou O -outro')
    print('- Cor dos olhos: (A - Azuis ou C - Castanhos)')
    print('- Cor dos cabelos: (L - Louros, P- Pretos ou C Castanhos)')
    print('- Idade: <inserir numero>')
    print('--------------------------------------------------------')
    counter = 0
    person_list = []
    while counter < 5:
        person_dict = {}
        counter += 1
        print(f'Preencha as informações para a {counter}a pessoa:') 
        gender = input('Gênero: ')
        eye_color = input('Cor dos olhos: ')
        hair_color = input('Cor dos cabelos: ')
        age = int(input('Idade: '))

        person_dict['Gender'] = gender.upper()
        person_dict['Eyes'] = eye_color.upper()
        person_dict['Hair'] = hair_color.upper()
        person_dict['Age'] = age
        person_list.append(person_dict)

    return person_list

def older_age(person_list):
    df = pd.DataFrame(person_list)
    max_age = max(df['Age'])
    print(f'A maior idade entre os habitantes é {max_age}')

def specific_woman(person_list):
    df = pd.DataFrame(person_list)
    seletion = df.loc[(df['Gender'] == 'F') & (df['Age'] >= 18) & (df['Age'] <= 35) & (df['Eyes'] == 'A') & (df['Hair'] == 'L')]
    print(f'Há {seletion.shape[0]} pessoa(s) do sexo feminino, loira(s) e com olhos azuis.')

def main():
    person_list = input_data()
    older_age(person_list)
    specific_woman(person_list)

# Teste
main()
