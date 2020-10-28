#Buris Mateo - Nuñez Matias

from TDA_Lista import *
from os import system
import sys

class Item():
    def __init__(self, value, key):
        self.value = value
        self.key = key

class Telefono():
    def __init__(self, apellido=None, nombre=None, caract=None, numero=None):
        self.apellido = apellido
        self.nombre = nombre
        self.caract = caract
        self.numero = numero

class Hashtable():
    def __init__(self, tamanio=100):
        self.tamanio_ = tamanio
        self.tabla = []
        for i in range(0, self.tamanio_):
            self.tabla.append(T_Lista())

    def f_hash(self, num):
        hashear = num.caract
        key = 0
        for i in range(0, len(hashear)):
            key += ord(hashear[i])
        return key % self.tamanio_


def cargar_tel():
    num = Telefono()
    num.apellido = input("Ingrese el apellido de la persona: ")
    num.nombre = input("Ingrese el nombre de la persona: ")
    num.caract = input("Ingrese la caracteristica telefonica: ")
    num.numero = input("Ingrese el numero telefonico: ")
    return num

def Menu(hash):

    seguir = True
    while seguir:
        print('')
        print('1. Insertar un numero')
        print('2. Eliminar un numero')
        print('3. Buscar un numero')
        print('4. Ver todos los num de una caracteristica')
        print('5. Salir')
        opc = input('Opcion: ')
        system('clear') #esto funciona para unix/linux, para windows es ('cls')
        if opc == '1':
            num = cargar_tel()
            punt = hash.f_hash(num)
            bus = busqueda(hash.tabla[punt], num.numero, 'numero')
            if bus is None:
                insertar(hash.tabla[punt], num, 'apellido')
                print('El numero se inserto correctamente')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
                system('clear')
            else:
                print('El telefono ya existe')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
                system('clear')
        if opc == '2':
            num = cargar_tel()
            punt = hash.f_hash(num)
            bus = busqueda(hash.tabla[punt], num.numero, 'numero')
            if bus != None:
                eliminar(hash.tabla[punt], num, 'numero')
                print('El numero se elimino correctamente')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
                system('clear')
            else:
                print('El numero no existe')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
                system('clear')

        if opc == '3':
            num = cargar_tel()
            punt = hash.f_hash(num)
            bus = busqueda(hash.tabla[punt], num.numero, 'numero')
            if bus is None:
                print('El numero no existe')
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
                system('clear')
            else:
                print('')
                print('Los datos son:')
                print('Apellido: ', bus.info.apellido)
                print('Nombre: ', bus.info.nombre)
                print('Numero Telefonico: ', bus.info.caract, '-', bus.info.numero)
                print('')
                print('Presione una tecla para continuar')
                tecla = sys.stdin.read(1)
                system('clear')

        if opc == '4':
            print('')
            num = Telefono()
            num.caract = input('Ingrese la caracteristica: ')
            bus = hash.f_hash(num)
            mostrar_telefonos(hash.tabla[bus])
            print('')
            print('Presione una tecla para continuar')
            tecla = sys.stdin.read(1)
            system('clear')

        if opc == '5':
            seguir = False
            system('clear')

h = Hashtable()
Menu(h)
