
'''simple iterador, que abre un archivo e itera sibre cada regla

Programar es disenar, y diseñar es siempre una continua eleccion entre
decisiones que presentan ventajas e inconvenientes.
'''

from Build import Aplicar_reglas as funcion


class Iterador(object):

    def __init__(self):
        self.archivo = open('datos/reglas.txt', encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.contador = 0
        return self

    def __next__(self):
        self.contador += 1
        if len(self.cache) >= self.contador:
            return self.cache[self.contador - 1]

        if self.archivo.closed:
            raise StopIteration

        linea = self.archivo.readline()
        if not linea:
            self.archivo.close()
            raise StopIteration

        pattern, buscar, remplazar = linea.split(None, 3)
        reglas = funcion(pattern, buscar, remplazar)
        self.cache.append(reglas)
        return reglas

