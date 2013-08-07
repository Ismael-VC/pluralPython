import re

''' Simple contructor de regras en plural
    del idioma ingles '''


def Aplicar_reglas(pattern, buscar, remplazar):
    ''' esta funcion busca y remplaza las palabras
        a plural '''

    def validar_reglas(palabra):
        return re.search(pattern, palabra)

    def aplicar_reglas(palabra):
        return re.sub(buscar, remplazar, palabra)
    return (validar_reglas, aplicar_reglas)
