import csv

def obtenerInformacion(ruta):
    costos = []
    with open(ruta, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            costos.append(line)
    return costos