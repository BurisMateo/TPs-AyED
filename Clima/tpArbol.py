import csv
from TDA_ArbolAVL import arbolAVL

def cargarArboles(datos, arbol=arbolAVL()):
    try:
        with open(datos) as File:
            reader = csv.reader(File, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)

            lista = ['idrisk', 'date', 'time', 'temperature', 'pressure', 'wind', 'humidity',
                    'weather', 'idname']

            for row in reader:
                if row != lista:
                    arbol.insert(row)

    except FileNotFoundError:
        print('¡Error, el fichero o directorio no existe!')
        raise



datos_clima_csv = 'datos_clima.csv'
arbol_datos_clima = arbolAVL()
cargarArboles(datos_clima_csv, arbol_datos_clima)
arbol_datos_clima.toString()