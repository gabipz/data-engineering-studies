"""
14. Altere o exercício anterior para que a função aceite um argumento de quantos sinais de igual serão mostrados. Ex: DesenhalLinha(4) tem como saída ====; DesenhalLinha(10) tem como saída ==========. No programa principal execute várias chamadas a essa função. (use um loop)
"""

def draw_line(size):
    counter = 0
    while counter < size:
        print('=',end="")
        counter += 1

if __name__ == "__main__":
    draw_line(4)
    print('\n')
    draw_line(10)

