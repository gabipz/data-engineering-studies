# Lista de exercícios

- [X] 1. Crie um programa que leia três números. Para cada número, imprima o dobro. Use uma função que recebe como parâmetro um número inteiro e devolve o seu dobro. O valor calculado deve ser impresso na função principal.
- [X] 2. Faça um programa receba dois números e execute as seguintes funções:
- Verificar se o número digitado é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo, O se negativo ou -1 se for igual a 0. Obedeça ao protótipo da função: ```int verifica(int num)```.
- Receber dois números inteiros positivos por parâmetro e retorne a soma dos N números inteiros existentes entre eles. ```int soma_entre(int num1, int num2)```.

- [X] 3. Faça uma função que receba por parâmetro dois valores X e Z. Calcule e retorne o resultado de X^2 para o programa principal. Atenção não utilize nenhuma função pronta de exponenciação.
- [X] 4. Crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medidas dos três lados de um triângulo. Elabore funções que:

 - Determinar se eles lados formam um triângulo, sabendo que:

	-   O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.    

	- Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo. Sendo que:

- Chama-se equilátero o triângulo que tem três lados iguais.

- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.

- Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

- [X] 5. Foi realizada um pesquisa de algumas características físicas de cinco habitantes de certa região. De cada habitante foram coletados os seguintes dados: sexo, cor dos olhos (A Azuis ou C - Castanhos), cor dos cabelos (L - Louros, P- Pretos ou C Castanhos) e idade. Faça uma função que leia esses dados em um vetor. Determine, por meio de outra função a média de idade das pessoas com olhos castanhos e cabelos pretos. Mostre esse resultado no programa principal.

- Faça uma função que determine e devolva ao programa principal a maior idade entre os habitantes.

- Faça uma função que determine e devolva ao programa principal a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros.

- [ ] 6. Os dois dígitos de verificação do CPF (constituído de 9 dígitos) são calculados através do algoritmo abaixo:
a) Etapa 1: cálculo de DV 1 
- Soma 1: soma dos produtos de cada dígito por um peso de 2 a 10, na ordem inversa (do nono para o primeiro). 
- Multiplique a soma 1 por 10 e calcule o resto da divisão do resultado por 11. Se der 10, DV1 é zero, caso contrário o DV1 é o próprio resto.
b) Etapa 2: cálculo de DV2 
- Soma 2: soma dos produtos de cada dígito por um peso de 3 a 11, também na ordem inversa.
- Adicione a Soma 2 ao dobro do DV1, multiplique por 10 e calcule o resto da divisão do resultado por 11. Se der 10, DV2 é zero, caso contrário o DV2 é o próprio resto.
c) Etapa 3: Multiplique DV1 por 10, some com DV2 e você tem o número de controle do CPF.
Exemplo: para o CPF 398 136 146, temos:
- Etapa 1: 2x6 + 3x4 + 4x1 + 5x6 + 6x3 + 7x1 + 8x8 + 9x9 + 10x3 = 258 2580 mod 11 = 6, portanto, DV1 = 6
- Etapa 2: 3x6 + 4x4 + 5x1 + 6x6 + 7x3 + 8x1 + 9x8 + 10x9 + 11x3 = 299 (299 + 6x2)x10 mod 11 = 3150 mod 11 = 8, portanto DV2 = 8.

- [ ] 7. Faça uma função chamada 'simplifica' que recebe como parâmetro o numerador e o denominador de uma fração. Esta função deve simplificar a fração recebida dividindo o numerador e o denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplifica para 3/5 dividindo o numerador e o denominador por 12. A função deve modificar as variáveis passadas como parâmetro. Faça uma função main para testar esta função. Dica: seja M o menor valor entre o numerador e o denominador. Para cada número primo de 2 até M, divida o numerador e o denominador por este primo enquanto for possível.

- [X] 8. Escrever um programa que obtenha a data atual (ler dia, mês e ano) e exiba-a na tela no formato textual por extenso. A escrita da data por extenso deve ser realizada por um procedimento separado. Exemplo: Data: 01/01/2000, Imprimir: Sábado, 1 de janeiro de 2000.
- [X] 9. Faça uma função que retorne o maior fator primo de um número.

- [X] 10. Faça um algoritmo que receba um número inteiro positivo n e calcule:

a) n!

b) Somatório de 1 até n

Obs.: Crie uma função para cada letra.

- [ ] 11. Faça um programa que faça operações simples de frações:
- Crie e leia duas frações p e q, compostas por numerador e denominador.
- Encontre o máximo divisor comum entre o numerador e o denominador, e simplifique as frações.
- Apresente a soma, a subtração, o produto e o quociente entre as frações lidas.
Obs.: Cria uma função para cada item.

- [X] 12. Faça uma função que receba um número N e retorne a soma dos algarismos de N!. Ex: se N = 4, N! = 24. Logo, a soma de seus algarismos é 2 + 4 = 6.

- [X] 13. Faça uma função chamada ```Desenhalinha```. Ela deve desenhar uma linha na tela usando vários símbolos de igual (Ex: ========). No programa principal execute várias chamadas a essa função. (use um loop)

- [X] 14. Altere o exercício anterior para que a função aceite um argumento de quantos sinais de igual serão mostrados. Ex: ```DesenhalLinha(4)``` tem como saída ====; ```DesenhalLinha(10)``` tem como saída ==========. No programa principal execute várias chamadas a essa função. (use um loop)

- [X] 15. Faça uma função ```Troque```, que recebe duas variáveis reais A e B e troca o valor delas (i.e., A recebe o valor de B e B recebe o valor de A).

- [ ] 16. A função fatorial duplo é definida como o produto de todos os números naturais impares de 1 até algum número natural impar N. Assim, o fatorial duplo de 5 é: ```5!! = 1*3*5= 15```.

Faça uma função não-recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.

- [ ] 17. O fatorial quádruplo de um número N é dado por:
				``` (2n)! / n! ```
				Faça uma função não-recursiva que receba um número inteiro positivo Ne retorne o fatorial quádruplo desse número.
  
- [ ] 18. O superfatorial de um número N é definida pelo produto dos N primeiros fatoriais de N. Assim, o superfatorial de 4 é ```sf(4) = 1! * 2! 3! 4! 288```.
Faça uma função não-recursiva que receba um número inteiro positivo N e retorne o superfatorial desse número.

- [ ] 19. Os números tribonacci são definidos pela seguinte recursão:
```
f(n) = 0 se n = 0
f(n) = 0 se n=1
f(n) = 1 se n=2
f(n) = f(n-1)=f(n-2)=f(n-3) se n>2.
```
Faça uma função não-recursiva que receba um número Ne retorne o N-ésimo termo da sequência de tribonacci.

- [ ] 20. Uma palavra de Fibonacci é definida por
``` 
f(n) = b se n=0
f(n) = a se n=1
f(n) = a se n = 1 f(n-1)+f(n-2) se n ≥2
```
Aqui + denota a concatenação de duas strings. Esta sequência inicia com as seguin tes palavras: b, a, ab, aba, abaab, abaababa, abaababaabaab, ... Faça uma função não-recursiva que receba um número N e retorne a N-ésima palavra de Fibonacci.

- [ ] 21. Construa um programa que receba da linha de comando, com a qual o programa é executado, dois operandos e um operador na notação infixada. O programa deve efetuar a operação de forma adequada, ou seja, levando em consideração os operandos envolvi dos. Exemplo (no caso do executável se chamar calcule):
```
	calcule 7.2 + 3 retorna 10.2
	calcule 3/-4 retorna 0
	calcule 3/ +4.0 retorna 0.75
	calcule 7 % 2.0 Operação inválida!  
	calcule 7 g 2.0 Operação inválida!
	calcule 7 * 2t Segundo operando inválido!
	calcule .62 - 4 Primeiro operando inválido!
```
- [ ] 22. Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo que o raio é passado por parâmetro.
 ```V=4/3 R³```

- [ ] 23. Crie um programa que contenha uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com pontos de exclamação, conforme o exemplo abaixo (para n = 5):
```
!
!!
!!!
!!!!  
!!!!!
```
- [ ] 24. Crie um programa contendo as seguintes funções que recebem um vetor V de 10 números reais como parâmetro:
- Impressão normal do vetor.

```{void imprime_normal (float vet [10])```

- Impressão inversa.
```void imprime_inversa (float vet [10])```

- Função que retorna a média aritmética dos elementos do vetor. 

```float media aritmetica (float vet [10])\\```

Observação: Tente obedecer ao protótipo das funções e para essas funções faça um programa.

- [ ] 25. Elabore um programa contendo uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média calculada deverá ser devolvida ao programa principal para então ser impressa na tela.

- [ ] 26. Faça um programa que apresente o menu a seguir, permita ao usuário escolher a opção desejada, receba os dados necessários para executar a operação e mostre o resultado.
Verifique a possibilidade de opção inválida. Use funções na escrita do programa. MENU
	- 1. Imposto
	- 2. Novo salário
	- 3. Classificação

a) OPCAO1 Mostrar a seguinte tabela relativa aos impostos: SALARIO PERCENTUAL DE IMPOSTO

- Menor que 500: 5%

- Entre 500 a 850: 15% Mais que 850: 20%

b) OPCAO2 receber o salário bruto do funcionário, e aplicar a dedução de imposto, segundo a tabela acima.

c) OPCAO3 mostrar a classificação do funcionário, de acordo com as seguintes regras: 

- Até 700 reais – mal remunerado;

- Maior que 700 reais - bem remunerado;

Caso o usuário selecione a opção 3, mas não tenha selecionado a opção 2, peça a ele para entrar com o valor do salário.  

- [ ] 27. Desenvolva um programa em Linguagem C que permita fazer as seguintes operações sobre um vetor que contém no máximo 100 números inteiros positivos. Use funções na escrita do programa. Apresente um menu aos usuários, com as seguintes opções:

a) Inserir um elemento em uma posição específica. O usuário informa a posição e o elemento.

b) Inserir um elemento no fim do array, ou seja, na última posição livre.  

c) Inserir um elemento no início do array, ou seja, na primeira posição livre.

d) Remover um elemento de uma posição específica. O usuário informa a posição.

e) Modificar o valor de um elemento de uma posição específica, fornecida pelo usuário. 

f) Exibir os elementos do vetor

Lembrete: inserções e remoções podem causar deslocamento dos elementos do array.

- [ ] 28. Escreva uma função para determinar a quantidade de números primos abaixo n.

- [ ] 29. Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos e segundos, e os converta em segundos.

