#Buris Mateo - Nuñez Matias

from TDA_Grafo import *
from os import system
import sys

def cargar_grafo(grafo):
    insertar_vertice(grafo, 'Buenos Aires')
    insertar_vertice(grafo, 'Catamarca')
    insertar_vertice(grafo, 'Chaco')
    insertar_vertice(grafo, 'Cordoba')
    insertar_vertice(grafo, 'Corrientes')
    insertar_vertice(grafo, 'Entre Rios')
    insertar_vertice(grafo, 'Formosa')
    insertar_vertice(grafo, 'Jujuy')
    insertar_vertice(grafo, 'La Pampa')
    insertar_vertice(grafo, 'Mendoza')
    insertar_vertice(grafo, 'Neuquen')
    insertar_vertice(grafo, 'Rio Negro')
    insertar_vertice(grafo, 'Salta')
    insertar_vertice(grafo, 'San Juan')
    insertar_vertice(grafo, 'Santa Fe')

    ori = buscar_vertice(grafo, 'Buenos Aires')
    des = buscar_vertice(grafo, 'Cordoba')
    insertar_arista(grafo, 9, ori, des)

    ori = buscar_vertice(grafo, 'Buenos Aires')
    des = buscar_vertice(grafo, 'Entre Rios')
    insertar_arista(grafo, 14, ori, des)

    ori = buscar_vertice(grafo, 'Buenos Aires')
    des = buscar_vertice(grafo, 'La Pampa')
    insertar_arista(grafo, 5, ori, des)

    ori = buscar_vertice(grafo, 'Entre Rios')
    des = buscar_vertice(grafo, 'Corrientes')
    insertar_arista(grafo, 12, ori, des)

    ori = buscar_vertice(grafo, 'Entre Rios')
    des = buscar_vertice(grafo, 'Santa Fe')
    insertar_arista(grafo, 174, ori, des)

    ori = buscar_vertice(grafo, 'Santa Fe')
    des = buscar_vertice(grafo, 'Chaco')
    insertar_arista(grafo, 95, ori, des)

    ori = buscar_vertice(grafo, 'Chaco')
    des = buscar_vertice(grafo, 'Formosa')
    insertar_arista(grafo, 11, ori, des)

    ori = buscar_vertice(grafo, 'Salta')
    des = buscar_vertice(grafo, 'Jujuy')
    insertar_arista(grafo, 52, ori, des)

    ori = buscar_vertice(grafo, 'Cordoba')
    des = buscar_vertice(grafo, 'Catamarca')
    insertar_arista(grafo, 60, ori, des)

    ori = buscar_vertice(grafo, 'Catamarca')
    des = buscar_vertice(grafo, 'Salta')
    insertar_arista(grafo, 57, ori, des)

    ori = buscar_vertice(grafo, 'La Pampa')
    des = buscar_vertice(grafo, 'Mendoza')
    insertar_arista(grafo, 143, ori, des)

    ori = buscar_vertice(grafo, 'La Pampa')
    des = buscar_vertice(grafo, 'Neuquen')
    insertar_arista(grafo, 20, ori, des)

    ori = buscar_vertice(grafo, 'Mendoza')
    des = buscar_vertice(grafo, 'San Juan')
    insertar_arista(grafo, 40, ori, des)

    ori = buscar_vertice(grafo, 'Neuquen')
    des = buscar_vertice(grafo, 'Rio Negro')
    insertar_arista(grafo, 22, ori, des)


def menu(grafo):
    seguir = True
    print('')
    print('¿Desea iniciar un grafo nuevo o cargar un grafo pre-creado?')
    print('1. Grafo nuevo')
    print('2. Cargar grafo')
    opc = input('Opcion: ')
    if (opc == '2'):
        cargar_grafo(grafo)
    while seguir:
        system('cls') #para que funcione en linux debe ser 'clear'
        print('Menu:')
        print('1. Insertar vertice')
        print('2. Insertar arista')
        print('3. Ver todos los vertices y sus adyacentes')
        print('4. Eliminar vertice')
        print('5. Eliminar arista')
        print('6. Mostrar el camino entre dos vertices')
        print('7. Salir')
        opc = input('Opcion: ')

        if (opc == '1'):
            system('cls')
            print('Ingrese los datos correspondientes')
            ver = input('Nombre del vertice: ')
            bus = buscar_vertice(grafo, ver)
            system('cls')
            if (bus != None):
                print('Este vertice ya existe')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
            else:
                insertar_vertice(grafo, ver)
                print('El vertice se inserto correctamente')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
        
        if (opc == '2'):
            system('cls')
            print('Ingrese los datos correspondientes')
            bus1 = input('Vertice origen: ')
            bus2 = input('Vertice destino: ')
            ori = buscar_vertice(grafo, bus1)
            des = buscar_vertice(grafo, bus2)
            if (ori != None) and (des != None):
                ari = input('Identificador de la arista: ')
                insertar_arista(grafo, ari, ori, des)
                system('cls')
                print('La arista se inserto correctamente')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
            else:
                system('cls')
                if (ori == None):
                    print('El vertice origen no existe')
                    print('')
                    print('Presione una tecla para continuar')
                    tecla = sys.stdin.read(1)
                if (des == None):
                    print('El vertice destino no existe')
                    print('')
                    print('Presione una tecla para continuar')
                    tecla = sys.stdin.read(1)

        if (opc == '3'):
            system('cls')
            if (grafo.tamanio == 0):
                print('No hay vertices en el grafo')
            else:
                barrido_vertices(grafo)
            print('')
            print('Presione una tecla para continuar')
            tecla = sys.stdin.read(1)
        
        if (opc == '4'):
            system('cls')
            print('Ingrese los datos correspondientes')
            ver = input('Nombre del vertice: ')
            bus = buscar_vertice(grafo, ver)
            system('cls')
            if (bus == None):
                print('Este vertice no existe')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
            else:
                eliminar_vertice(grafo, ver)
                print('El vertice se elimino correctamente')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)

        if (opc == '5'):
            system('cls')
            print('Ingrese los datos correspondientes')
            bus1 = input('Vertice origen: ')
            bus2 = input('Vertice destino: ')
            ori = buscar_vertice(grafo, bus1)
            des = buscar_vertice(grafo, bus2)
            if (ori != None) and (des != None):
                eliminar_arista(grafo, ori, bus2)
                system('cls')
                print('La arista se elimino correctamente')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
            else:
                system('cls')
                if (ori == None):
                    print('El vertice origen no existe')
                    print('')
                    print('Presione una tecla para continuar')
                    tecla = sys.stdin.read(1)
                if (des == None):
                    print('El vertice destino no existe')
                    print('')
                    print('Presione una tecla para continuar')
                    tecla = sys.stdin.read(1)
        
        if (opc == '6'):
            system('cls')
            print('Ingrese los datos correspondientes')
            bus1 = input('Vertice origen: ')
            bus2 = input('Vertice destino: ')
            ori = buscar_vertice(grafo, bus1)
            des = buscar_vertice(grafo, bus2)
            if (ori != None) and (des != None):
                buscar_camino(grafo, bus1, bus2)
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
            else:
                system('cls')
                if (ori == None):
                    print('El vertice origen no existe')
                    print('')
                    print('Presione una tecla para continuar')
                    tecla = sys.stdin.read(1)
                if (des == None):
                    print('El vertice destino no existe')
                    print('')
                    print('Presione una tecla para continuar')
                    tecla = sys.stdin.read(1)

        if (opc == '7'):
            seguir = False
            system('cls')


G = Grafo(False)
menu(G)