import random
    
def insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        
        while j >=0 and key < lista[j] :
                lista[j+1] = lista[j]
                j -= 1
        lista[j+1] = key

    return lista


def seleccion(lista):
    for i in range(len(lista)-1):
        min_index = i
        
        for j in range(i+1, len(lista)-1):
            if lista[j] < lista[min_index]:
                min_index = j
                
        lista[i], lista[min_index] = lista[min_index], lista[i]
        
    return lista

    
def burbuja(lista):
    n = len(lista)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

def burbuja_optimizado(lista):
    n = len(lista)
    isSwap = True
    
    for i in range(n-1):
        if isSwap:
            isSwap = False
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1] :
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    isSwap = True
        else:
            return lista
    
    return lista

def quicksort_mejor(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[((len(lista)-1)//2)]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return quicksort_mejor(izquierda)+centro+quicksort_mejor(derecha)
    else:
      return lista

def quicksort_peor(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return quicksort_peor(izquierda)+centro+quicksort_peor(derecha)
    else:
      return lista
 
def quicksort_promedio(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[random.randint(0,len(lista)-1)]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return quicksort_promedio(izquierda)+centro+quicksort_promedio(derecha)
    else:
      return lista

# Función merge
def merge(lista1, lista2):
    
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
 
   # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
 
   # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]
 
    # Retornamos el resultados
    return result

def merge_sort(lista):
   
   if len(lista) < 2:
      return lista
    
    # De lo contrario, se divide en 2
   else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)


