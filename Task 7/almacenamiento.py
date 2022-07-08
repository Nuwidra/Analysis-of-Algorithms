def maximizar(As, D):
    As = heap_sort(As)
    M = []
    for i in range (0, len(As)-1):
        D -= As[i][1]
        if D > 0:
            M.append(As[i]) 
        else:
            return M 


def heapify(As, heap_size, root_index):
  
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2

    if left_child < heap_size and As[largest][1] < As[left_child][1]:
        largest = left_child

    if right_child < heap_size and As[largest][1] < As[right_child][1]:
        largest = right_child

    if largest != root_index:
        As[root_index], As[largest] = As[largest], As[root_index]

        heapify(As, heap_size, largest)


def heap_sort(As):
    n = len(As)

    for i in range(n//2 - 1, -1, -1):
        heapify(As, n, i)

    for i in range(n - 1, 0, -1):
        As[i], As[0] = As[0], As[i]
        heapify(As, i, 0)

    return As
 
 # Referencia del algoritmo: 
 # https://stackabuse.com/sorting-algorithms-in-python/#sortinginpython