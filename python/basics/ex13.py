"""
13. Faça uma função chamada Desenhalinha. Ela deve desenhar uma linha na tela usando vários símbolos de igual (Ex: ========). No programa principal execute várias chamadas a essa função. (use um loop)
"""

def draw_line():
    counter = 0
    while counter <= 8:
        print('=',end="")
        counter += 1

if __name__ == "__main__":
    draw_line()

