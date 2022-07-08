[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4148238&assignment_repo_type=AssignmentRepo)
# IC-3002 Tarea corta 0

Considere el siguiente problema computacional

**Problema**: Determinar si un número es primo
* **Entradas**: Un número ![n perteneciente a los naturales](https://latex.codecogs.com/png.latex?n%20%5Cin%20%5Cmathbb%7BN%7D)
* **Salidas**: ![Si](https://latex.codecogs.com/png.latex?Si) cuando ![n](https://latex.codecogs.com/png.latex?n) es primo, ![No](https://latex.codecogs.com/png.latex?No) en cualquier otro caso.

Implemente la función `es_primo` con un algoritmo que resuelva el problema.

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
