#Buris Mateo - Nuñez Matias

def criterio(dato, clave):
    if(clave==None):
        return dato
    elif(clave=='numero'):
        return dato.numero
    elif(clave=='apellido'):
        return dato.apellido
    elif(clave=='nombre'):
        return dato.nombre

class NodoLista():
    def __init__(self):
        self.info = None
        self.sig = None

class T_Lista():
    def __init__(self):
        self.tamanio = 0
        self.cab = None

def insertar(self, x, crit=None):
    self.tamanio = self.tamanio+1
    aux = NodoLista()
    aux.info = x
    if (self.cab==None) or (criterio(x, crit) < criterio(self.cab.info, crit)):
        aux.sig = self.cab
        self.cab = aux
    else:
        ant = self.cab
        act = self.cab.sig
        while (act != None) and (criterio(act.info,crit) < criterio(x, crit)):
            act = act.sig
            ant = ant.sig
        aux.sig = act
        ant.sig = aux

def eliminar(self, ku, crit=None):
    x = None
    if (criterio(self.cab.info,crit)==ku):
        x = self.cab.info
        self.cab = self.cab.sig
        self.tamanio=self.tamanio-1
    else:
        ant = self.cab
        act = self.cab.sig
        while((act != None)and(criterio(act.info,crit) != ku)):
            ant=ant.sig
            act=act.sig
        if(act != None):
            x = act.info
            ant.sig = act.sig
            self.tamanio = self.tamanio-1
        return x

def busqueda(self, ku, clave=None):
    pos = self.cab
    while((pos != None) and (criterio(pos.info,clave) != ku)):
        pos = pos.sig
    return pos

def tamanio(self):
    return self.tamanio

def listavacia(self):
    if self.tamanio==0:
        return True
    else:
        return False

def mostrar(self):
    nodo = self.cab
    while nodo != None:
        print(nodo.info)
        nodo = nodo.sig

def mostrar_telefonos(self):
    nodo = self.cab
    while nodo != None:
        print('')
        print('Datos del usuario:')
        print('Apellido: ', nodo.info.apellido)
        print('Nombre: ', nodo.info.nombre)
        print('Numero Telefonico: ',nodo.info.caract, "-", nodo.info.numero)
        print('')
        nodo = nodo.sig

'''
lista=T_Lista()
if listavacia(lista):
    print('si')
else:
    print('no')
insertar(lista, 9)
insertar(lista, 13)
insertar(lista, 3)
mostrar(lista)
x=busqueda(lista,9)
if(x!=None):
    print('encuentra')
else:
    print('no encuentra')

if listavacia(lista):
    print('si')
else:
    print('no')
'''
