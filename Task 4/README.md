[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4395128&assignment_repo_type=AssignmentRepo)
# IC-3002 Tarea corta 5

Considere el siguiente problema computacional:

**Problema**: Ordenar una secuencia de números enteros.
* **Entradas**: ![](https://latex.codecogs.com/png.latex?%28A%2Cn%29) tal que ![](https://latex.codecogs.com/png.latex?A%20%3D%20%28a_1%2C%20a_2%2C%20%5Cdots%2C%20a_n%7Ca_k%20%5Cin%20%5Cmathbb%7BZ%7D%29%20%5Cland%20n%20%3D%20%7CA%7C)
* **Salidas**: La secuencia ![](https://latex.codecogs.com/png.latex?A) ordenada de manera tal que ![](https://latex.codecogs.com/png.latex?%5Cunderset%7B0%20%5Cleq%20i%20%3C%20j%20%3C%20n%7D%20%7B%5Cforall%20i%2C%20j%7D%20%3A%20a_i%20%5Cleq%20a_j)


Este problema se puede resolver, entre otras opciones, con el algoritmo de ordenamiento por burbuja. En el archivo `burbuja.py`, la función `burbuja` implementa dicho algoritmo sobre una lista.

1. Implemente en el archivo `burbuja.py` la función `burbuja_optimizado` como una mejora a la función `burbuja` tomando en cuenta que si en un recorrido no hizo intercambios es porque la lista ya está ordenada.

2. Implemente en el archivo `burbuja_test.py` las funciones `test_mejor_caso`, `test_peor_caso`, `test_caso_promedio` para probar correspondientemente los casos mejor, peor y promedio de `burbuja_optimizado`. Cada prueba debe verificar la complejidad temporal esperada para el caso correspondiente.

**Importante**: para poder verificar la complejidad temporal utilizando la biblioteca `big_O`, debe programar funciones `generar_mejor(n)`, `generar_peor(n)` y `generar_promedio(n)` que retornan, cada una, una lista de enteros de tamaño `n` cuyo contenido representa una instancia del caso.

## Cómo instalar el ambiente de desarrollo y ejecutar las pruebas localmente

Este proyecto requiere `python3`. Asegúrese que esté instalado en su distribución de linux.

Si no lo ha hecho anteriormente, crear un ambiente virtual para las dependencias

```bash
python3 -m venv .venv
```

Activar el ambiente virtual

```bash
source .venv/bin/activate
```

Instalar las dependencias

```bash
pip3 install -r requirements.txt
```

```bash
pip3 install gnuplotlib
```

Ejecutar las pruebas

```bash
pytest -s -W ignore::DeprecationWarning
```

## Rúbrica

### Completitud (5 pts)

* (5 pts) La producción cumple totalmente con los requerimientos solicitados.
* (3 pts) La producción cumple parcialmente con los requerimientos solicitados.
* (1 pts) La producción, en su mayor parte, no cumple con los requerimientos solicitados.

### Correctitud (5 pts)

* (5 pts) El código pasa exitosamente todas las pruebas automatizadas.
* (3 pts) El código pasa la mayoría de las pruebas automatizadas.
* (1 pts) El código no pasa la mayoría de las pruebas automatizadas.

### Optimización (5 pts)

* (5 pts) El código optimizado mejora el tiempo de ejecución del código original.
* (3 pts) El código optimizado corre en un tiempo de ejecución semejante al del código original.
* (1 pts) El código optimizado empeora el tiempo de ejecución del código original.
