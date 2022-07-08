import random

def generar_mejor_caso(n):
    lista = list(range(n))
    return lista

def generar_peor_caso(n):
    lista = list(range(n))
    lista.reverse()
    return lista

def generar_caso_promedio(n):
    lista = list(range(n))
    random.shuffle(lista)
    return lista

