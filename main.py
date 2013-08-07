from iterador import Iterador
import sys

reglas = Iterador()


def main(x):
    for validar, sub in reglas:
        if validar(x):
            return sub(x)
    raise ValueError('No se puede combertir la palabra \
                     {0} al plural'.format(x))


#ejemplo: python3 main.py frase_a_combertir

if __name__ == '__main__':
    try:
        cmd = sys.argv[1]
        if cmd:
            c = 'el plural de {0} es: '.format(cmd)
            print(c, (main(cmd)))
        else:
            print('comando no valido')
            print('#ejemplo: python3 main.py frase_a_combertir')
    except IndexError:
        print('intente esto: #ejemplo: python3 main.py frase_a_combertir')
