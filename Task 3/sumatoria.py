def sumatoria_cubica(n):
  resultado = 0
  for i in range(1, n+1):
    for j in range(1, i+1):
      for k in range(j, (j + i)+1):
        resultado = resultado + 1
  return resultado


def sumatoria_constante(n):
  resultado = n*(n+1)*(n+2)/3
  return resultado



