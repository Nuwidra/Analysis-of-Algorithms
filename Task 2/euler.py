
def e_cuadratica(n):
  sumatoria = 0
  
  for i in range(n):
    factorial = 1

    for i in range(1, n):
      if n >= 1:
        factorial = factorial * i
    n = n - 1
    sumatoria = sumatoria + 1/(factorial)

  return sumatoria

def e_lineal(n):

  sumatoria = 0
  factorial = 1
  
  for n in range(n):
    if n >= 1:

      factorial = factorial * n
      n = n - 1
      sumatoria = sumatoria + 1/(factorial)
    else:
      sumatoria = sumatoria + 1

  return sumatoria

