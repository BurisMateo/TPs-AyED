#Buris Mateo - Nuñez Matias

from TDA_Lista import *
from TDA_Pila import *

class nodoArista(object):
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None


class nodoVertice(object):
    def __init__(self, info, datos=None):
        self.info = info
        self.datos = datos
        self.sig = None
        self.adyacentes = Arista()


class Grafo(object):
    def __init__(self, dirigido=True):
        self.cab = None
        self.dirigido = dirigido
        self.tamanio = 0


class Arista(object):
    def __init__(self):
        self.cab = None
        self.tamanio = 0


def insertar_vertice(grafo, dato, datos=None):
    nodo = nodoVertice(dato, datos)
    if (grafo.cab is None or grafo.cab.info > dato):
        nodo.sig = grafo.cab
        grafo.cab = nodo
    else:
        ant = grafo.cab
        act = grafo.cab.sig
        while(act is not None and act.info < nodo.info):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1

def insertar_arista(grafo, dato, origen, destino):
    agregrar_arista(origen.adyacentes, dato, destino.info)
    if(not grafo.dirigido):
        agregrar_arista(destino.adyacentes, dato, origen.info)

def agregrar_arista(origen, dato, destino):
    nodo = nodoArista(dato, destino)
    if (origen.cab is None or origen.cab.destino > destino):
        nodo.sig = origen.cab
        origen.cab = nodo
    else:
        ant = origen.cab
        act = origen.cab.sig
        while(act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1

def eliminar_vertice(grafo, clave):
    ver = buscar_vertice(grafo, clave)
    x = None
    
    aux = grafo.cab
    while(aux is not None):
        ady = aux.adyacentes.cab
        while (ady is not None):
            if(ady.destino == clave):
                eliminar_arista(grafo, aux, clave)
            ady = ady.sig
        aux = aux.sig

    if(grafo.cab.info == clave):
        x = grafo.cab.info
        grafo.cab = grafo.cab.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.cab
        act = grafo.cab.sig
        while(act is not None and act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    return x


def quitar_arista(vertice, destino):
    x = None
    if(vertice.adyacentes.cab.destino == destino):
        x = vertice.adyacentes.cab.info
        vertice.adyacentes.cab = vertice.adyacentes.cab.sig
        vertice.adyacentes.tamanio -= 1
    else:
        ant = vertice.adyacentes.cab
        act = vertice.adyacentes.cab.sig
        while(act is not None and act.destino != destino):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            vertice.adyacentes.tamanio -= 1
    return x

def eliminar_arista(grafo, vertice, destino):
    x = quitar_arista(vertice, destino)    
    
    if(not grafo.dirigido):
        ori = buscar_vertice(grafo, destino)
        quitar_arista(ori, vertice.info)

    return x

def barrido_vertices(grafo):
    aux = grafo.cab
    while(aux is not None):
        print('vertice:', aux.info)
        print('adyacentes:')
        adyacentes(aux)
        print('')
        aux = aux.sig


def buscar_vertice(grafo, buscado):
    aux = grafo.cab
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux

def buscar_arista(vertice, buscado):
    aux = vertice.adyacentes.cab
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux

def tamanio(grafo):
    return grafo.tamanio

def grafo_vacio(grafo):
    return grafo.cab is None

def adyacentes(vertice):
    aux = vertice.adyacentes.cab
    if(aux is None):
        print('no tiene adyacentes')
    while(aux is not None):
        print(aux.destino, aux.info)
        aux = aux.sig


def buscar_camino(grafo, origen, destino, crit=None):
    pila=T_Pila()
    lista=T_Lista()
    pos = busqueda(grafo, origen)
    pos1 = busqueda(grafo, destino)
    apilar(pila,pos)
    control=False
    if (pos!=None) and (pos1!=None):
        while not pilaVacia(pila) and control==False:
            dato=desapilar(pila)
            posarc = buscar_arista(dato, destino)
            if (posarc!=None):
                apilar(pila,dato)
                apilar(pila,pos1)
                control=True
            else:
                if (dato.adyacentes!=None):
                    apilar(pila,dato)
                    insertar(lista,dato.info)
                    aux=dato.adyacentes.cab
                    while (aux!=None) and (busqueda(lista,aux.destino)!=None):
                        aux=aux.sig
                    if (aux!=None):
                        paux=buscar_vertice(grafo, aux.destino)
                        apilar(pila, paux)
                    else:
                        desapilar(pila)
    if not pilaVacia(pila):
        pila2 = T_Pila()
        print('el camino es:')
        while(not pilaVacia(pila)):
            x=desapilar(pila)
            apilar(pila2, x)
        while(not pilaVacia(pila2)):
            x=desapilar(pila2)
            print(x.info)
    else:
        print('No hay camino')

"""
G = Grafo(False)

insertar_vertice(G, 'Buenos Aires')
insertar_vertice(G, 'Entre Rios')
insertar_vertice(G, 'Mendoza')
insertar_vertice(G, 'La Pampa')
insertar_vertice(G, 'Jujuy')

ori = buscar_vertice (G, 'Buenos Aires')
des = buscar_vertice (G, 'Entre Rios')
insertar_arista(G, 1, ori, des)

ori = buscar_vertice (G, 'Buenos Aires')
des = buscar_vertice (G, 'Mendoza')
insertar_arista(G, 2, ori, des)

ori = buscar_vertice (G, 'Mendoza')
des = buscar_vertice (G, 'La Pampa')
insertar_arista(G, 3, ori, des)

ori = buscar_vertice (G, 'Buenos Aires')
des = buscar_vertice (G, 'Jujuy')
#insertar_arista(G, 4, ori, des)

ori = buscar_vertice (G, 'Entre Rios')
des = buscar_vertice (G, 'La Pampa')
insertar_arista(G, 5, ori, des)

ori = buscar_vertice (G, 'La Pampa')
des = buscar_vertice (G, 'Jujuy')
insertar_arista(G, 6, ori, des)

#buscar_camino(G, 'Entre Rios', 'Jujuy')
eliminar_vertice(G, ori)
#eliminar_arista(G, ori, 'Jujuy')
barrido_vertices(G)
"""