def fact(n):
    acum = 1
    for i in range(1, n + 1):
        acum *= i
    
    return acum
