class Nodo:
    def __init__(self, clave=None):
        self.clave = clave
        self.hijo_izquierdo = None
        self.hijo_derecho = None
        self.padre = None  # puntero al nodo padre en el árbol
        self.altura = 1  # altura del nodo en árbol NUEVO PARA A

class arbolAVL:
    strArbol = ""

    def __init__(self):
        self.raiz = None

    def insertar(self, clave):

        if self.raiz == None:
            self.raiz = Nodo(clave)
        else:
            self._insertar(clave, self.raiz)

    def _insertar(self, clave, nodo_actual):

        if clave < nodo_actual.clave:

            if nodo_actual.hijo_izquierdo == None:
                nodo_actual.hijo_izquierdo = Nodo(clave)
                nodo_actual.hijo_izquierdo.padre = nodo_actual  # set padre
                self._inspeccionar_insercion(nodo_actual.hijo_izquierdo)

            else:
                self._insertar(clave, nodo_actual.hijo_izquierdo)

        elif clave > nodo_actual.clave:
            if nodo_actual.hijo_derecho == None:
                nodo_actual.hijo_derecho = Nodo(clave)
                nodo_actual.hijo_derecho.padre = nodo_actual  # set padre
                self._inspeccionar_insercion(nodo_actual.hijo_derecho)

            else:
                self._insertar(clave, nodo_actual.hijo_derecho)
        else:
            print("¡La clave ya esta en el árbol!")

    def _altura(self, nodo_actual, altura_actual):

        if nodo_actual == None:
            return altura_actual

        altura_izquierda = self._altura(
            nodo_actual.hijo_izquierdo, altura_actual + 1)
        altura_derecha = self._altura(
            nodo_actual.hijo_derecho, altura_actual + 1)

        return max(altura_izquierda, altura_derecha)

    def altura(self):

        if self.raiz != None:
            return self._altura(self.raiz, 0)

        else:
            return 0


    def toString(self):
        if self.raiz != None:
            self._to_string(self.raiz)
            print("{%s}" % self.strArbol[:-2])

    def _to_string(self, nodo_actual):
        if nodo_actual != None:
            self._to_string(nodo_actual.hijo_izquierdo)
            self.strArbol += '%s, ' % str(nodo_actual.clave)
            self._to_string(nodo_actual.hijo_derecho)

    def _rebalance_nodo(self, z, y, x):

        if y == z.hijo_izquierdo and x == y.hijo_izquierdo:
            self._rotar_derecha(z)

        elif y == z.hijo_izquierdo and x == y.hijo_derecho:
            self._rotar_izquierda(y)
            self._rotar_derecha(z)

        elif y == z.hijo_derecho and x == y.hijo_derecho:
            self._rotar_izquierda(z)

        elif y == z.hijo_derecho and x == y.hijo_izquierdo:
            self._rotar_derecha(y)
            self._rotar_izquierda(z)

        else:
            raise Exception(
                '_rebalance_nodo: configuración de nodo z, y, x no reconocida!')

    def _inspeccionar_insercion(self, nodo_actual, camino=[]):

        if nodo_actual.padre == None:
            return

        camino = [nodo_actual] + camino

        altura_izquierda = self.get_altura(nodo_actual.padre.hijo_izquierdo)
        altura_derecha = self.get_altura(nodo_actual.padre.hijo_derecho)

        if abs(altura_izquierda - altura_derecha) > 1:
            camino = [nodo_actual.padre] + camino
            self._rebalance_nodo(camino[0], camino[1], camino[2])

            return

        nueva_altura = 1 + nodo_actual.altura

        if nueva_altura > nodo_actual.padre.altura:

            nodo_actual.padre.altura = nueva_altura

        self._inspeccionar_insercion(nodo_actual.padre, camino)
        
   
    def _rotar_derecha(self, z):

        sub_raiz = z.padre
        y = z.hijo_izquierdo
        t3 = y.hijo_derecho
        y.hijo_derecho = z
        z.padre = y
        z.hijo_izquierdo = t3

        if t3 != None:
            t3.padre = z
        y.padre = sub_raiz

        if y.padre == None:
            self.raiz = y

        else:
            if y.padre.hijo_izquierdo == z:
                y.padre.hijo_izquierdo = y

            else:
                y.padre.hijo_derecho = y
        z.altura = 1 + max(self.get_altura(z.hijo_izquierdo),
                           self.get_altura(z.hijo_derecho))
        y.altura = 1 + max(self.get_altura(y.hijo_izquierdo),
                           self.get_altura(y.hijo_derecho))

    def _rotar_izquierda(self, z):

        sub_raiz = z.padre
        y = z.hijo_derecho
        t2 = y.hijo_izquierdo
        y.hijo_izquierdo = z
        z.padre = y
        z.hijo_derecho = t2

        if t2 != None:
            t2.padre = z
        y.padre = sub_raiz

        if y.padre == None:
            self.raiz = y

        else:
            if y.padre.hijo_izquierdo == z:
                y.padre.hijo_izquierdo = y

            else:
                y.padre.hijo_derecho = y
        z.altura = 1 + max(self.get_altura(z.hijo_izquierdo),
                           self.get_altura(z.hijo_derecho))
        y.altura = 1 + max(self.get_altura(y.hijo_izquierdo),
                           self.get_altura(y.hijo_derecho))

    def get_altura(self, nodo_actual):

        if nodo_actual == None:
            return 0

        return nodo_actual.altura

    
    def encontrar(self, clave):
        if self.raiz != None:
            return self._encontrar(clave, self.raiz)
        else:
            return None

    def _encontrar(self, clave, nodo_actual):
        if clave == nodo_actual.clave:
            return nodo_actual


    def buscar(self, clave):

        if self.raiz != None:
            return self._buscar(clave, self.raiz)

        else:
            return False

    def _buscar(self, clave, nodo_actual):

        if clave == nodo_actual.clave:
            return True

        elif clave < nodo_actual.clave and nodo_actual.hijo_izquierdo != None:
            return self._buscar(clave, nodo_actual.hijo_izquierdo)

        elif clave > nodo_actual.clave and nodo_actual.hijo_derecho != None:
            return self._buscar(clave, nodo_actual.hijo_derecho)

        return False