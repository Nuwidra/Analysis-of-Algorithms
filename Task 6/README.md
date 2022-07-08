[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4763173&assignment_repo_type=AssignmentRepo)
# IC-3002 Tarea corta 8

Suponga que estamos construyendo una aplicación de software para automatizar la selección de rutas para movilización en bicicleta a través de una ciudad.

Sabemos que la movilidad en bicicleta es peligrosa en nuestras ciudades,pues la mayoría no cuenta con infraestructura adecuada, y aún no se ha normalizado una cultura de respeto entre los distintos actores que comparten las vías. Después de un análisis hemos identificado una serie de intersecciones consideradas particularmente peligrosas para la movilidad en bicicleta, por ejemplo debido al alto tránsito, la falta de visibilidad, o la falta de espacio en la vía, entre otras posibles causas.

Considere el mapa de la ciudad modelado como una cuadrícula de tamaño ![`X * Y`](https://latex.codecogs.com/png.latex?X%20%5Ctimes%20Y), cada casilla de esta cuadrícula representa una intersección entre dos o más calles. La casilla contiene una bandera levantada (modelada con un `1`) cuando se ha identificado como peligrosa, en cualquier otro caso la casilla contiene un `0`.

Tomando en cuenta que sólo se admiten movimientos horizontales y verticales (mas no diagonales), sabemos que si en la cuadrícula de la ciudad no hubiera intersecciones peligrosas, la ruta más corta siempre sería de longitud ![`X + Y - 1`](https://latex.codecogs.com/png.latex?X%20&plus;%20Y%20-%201) y habrían muchas de estas rutas. El problema que queremos resolver es determinar **cuántas** rutas de longitud ![`X + Y - 1`](https://latex.codecogs.com/png.latex?X%20&plus;%20Y%20-%201) se pueden encontrar dada una matriz que puede contener cero o más intersecciones peligrosas.

En términos computacionales establecemos el problema:

**Problema**: Dada una matriz ![`C`](https://latex.codecogs.com/png.latex?C) de tamaño ![`X * Y`](https://latex.codecogs.com/png.latex?X%20%5Ctimes%20Y) tal que ![cada casilla contiene un `1` un `0`](https://latex.codecogs.com/png.latex?%5Cunderset%7B0%20%5Cleq%20y%20%3C%20Y%7D%7B%5Cunderset%7B0%20%5Cleq%20x%20%3C%20X%7D%7B%5Cforall%20x%2C%20y%7D%7D%20%3A%20C_%7Bx%2Cy%7D%20%5Cin%20%5C%7B0%2C%201%5C%7D), encontrar cuántas rutas de longitud ![`X + Y - 1`](https://latex.codecogs.com/png.latex?X%20&plus;%20Y%20-%201) existen entre ![`C00`](https://latex.codecogs.com/png.latex?C_%7B0%2C0%7D) y ![`CXY`](https://latex.codecogs.com/png.latex?C_%7BX-1%2CY-1%7D)
* **Entradas**: La matriz ![`C`](https://latex.codecogs.com/png.latex?C).
* **Salidas**: ![`|Rs|`](https://latex.codecogs.com/png.latex?%7CRs%7C) tal que ![](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cdpi%7B150%7D%20%5Ctiny%20%5Cforall%20R%20%5Cin%20Rs%20%3A%20R%20%3D%20%5C%7B%280%2C0%29%2C%28i_1%2Cj_1%29%2C%5Cdots%2C%28i_k%2Cj_k%29%2C%28X-1%2CY-1%29%5C%7D%20%5Cland%20%5Cforall%20%28i%2Cj%29%20%5Cin%20R%20%3A%20C_%7Bi%2Cj%7D%20%3D%200%20%5Cland%20%7CR%7C%20%3D%20X%20&plus;%20Y%20-%201)

1. En el archivo `rutas.py`, implemente la función `contar_rutas_mas_cortas(C)` con un algoritmo que resuelva el problema planteado utilizando la técnica de programación dinámica en complejidad temporal ![`O(XY)`](https://latex.codecogs.com/png.latex?%5Cmathcal%7BO%7D%28XY%29).

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

* (5 pts) El código implementa un algoritmo de programación dinámica y corre en la complejidad temporal especificada.
* (3 pts) El código implementa un algoritmo de programación dinámica  pero no corre en la complejidad temporal especificada.
* (1 pts) El código no implementa un algoritmo de programación dinámica.
