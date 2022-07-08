[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4730236&assignment_repo_type=AssignmentRepo)
# IC-3002 Tarea corta 7

Suponga que estamos construyendo una aplicación de software para automatizar la selección de rutas para movilización en bicicleta a través de una ciudad.

Sabemos que la movilidad en bicicleta es peligrosa en nuestras ciudades,pues la mayoría no cuenta con infraestructura adecuada, y aún no se ha normalizado una cultura de respeto entre los distintos actores que comparten las vías. Después de un análisis hemos identificado una serie de intersecciones consideradas particularmente peligrosas para la movilidad en bicicleta, por ejemplo debido al alto tránsito, la falta de visibilidad, o la falta de espacio en la vía, entre otras posibles causas.

Considere el mapa de la ciudad modelado como una cuadrícula de tamaño ![`X * Y`](https://latex.codecogs.com/png.latex?X%20%5Ctimes%20Y), cada casilla de esta cuadrícula representa una intersección entre dos o más calles. La casilla contiene una bandera levantada (modelada con un `1`) cuando se ha identificado como peligrosa, en cualquier otro caso la casilla contiene un `0`.

El problema que queremos resolver es encontrar una ruta entre la casilla superior izquierda y la casilla inferior derecha de la cuadrícula, evitando pasar por las intersecciones peligrosas. No es posible moverse de manera diagonal entre casillas, sólo es posible moverse de manera horizontal o vertical.

En términos computacionales establecemos el problema:

**Problema**: Dada una matriz ![`C`](https://latex.codecogs.com/png.latex?C) de tamaño ![`X * Y`](https://latex.codecogs.com/png.latex?X%20%5Ctimes%20Y) tal que ![cada casilla contiene un `1` un `0`](https://latex.codecogs.com/png.latex?%5Cunderset%7B0%20%5Cleq%20y%20%3C%20Y%7D%7B%5Cunderset%7B0%20%5Cleq%20x%20%3C%20X%7D%7B%5Cforall%20x%2C%20y%7D%7D%20%3A%20C_%7Bx%2Cy%7D%20%5Cin%20%5C%7B0%2C%201%5C%7D), encontrar una ruta entre ![`C00`](https://latex.codecogs.com/png.latex?C_%7B0%2C0%7D) y ![`CXY`](https://latex.codecogs.com/png.latex?C_%7BX-1%2CY-1%7D)
* **Entradas**: La matriz ![`C`](https://latex.codecogs.com/png.latex?C).
* **Salidas**: Una matriz ![`R`](https://latex.codecogs.com/png.latex?R) de tamaño ![`X * Y`](https://latex.codecogs.com/png.latex?X%20%5Ctimes%20Y) tal que ![cada casilla contiene un `1` un `0`](https://latex.codecogs.com/png.latex?%5Cunderset%7B0%20%5Cleq%20j%20%3C%20Y%7D%7B%5Cunderset%7B0%20%5Cleq%20i%20%3C%20X%7D%7B%5Cforall%20i%2Cj%7D%7D%20%3A%20R_%7Bi%2Cj%7D%20%5Cin%20%5C%7B0%2C1%5C%7D%20%5Cland%20%28R_%7Bi%2Cj%7D%20%3D%201%20%5CRightarrow%20C_%7Bi%2Cj%7D%20%3D%200%29) donde cada ![`1`](https://latex.codecogs.com/png.latex?1) representa un paso en el camino encontrado, o ![vacío](https://latex.codecogs.com/png.latex?%5Cvarnothing) en caso de que no encuentre una ruta.

1. En el archivo `rutas.py`, implemente la función `encontrar_ruta(C)` con un algoritmo que resuelva el problema planteado utilizando la técnica de *backtracking*.

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

### Diseño del algoritmo (5 pts)

* (5 pts) El código implementa un algoritmo de backtracking.
* (1 pts) El código no implementa un algoritmo de backtracking.
