class Node:
    def __init__(self, key):
        self.key  =  key
        self.left =  None
        self.right = None
        self.father = None
        self.height= 1

class arbolAVL:
    strArbol = ""
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def get_altura(self, nodo_actual):
            if nodo_actual == None:
                return 0

            return nodo_actual.height

    def _insert(self, key, nodo_actual):
        if key < nodo_actual.key:
            if nodo_actual.left == None:
                nodo_actual.left = Node(key)
                nodo_actual.left.father = nodo_actual
                self._inspeccionar_insercion(nodo_actual.left)
            else:
                self._insert(key, nodo_actual.left)
        elif key > nodo_actual.key:
            if nodo_actual.right == None:
                nodo_actual.right = Node(key)
                nodo_actual.right.father = nodo_actual 
                self._inspeccionar_insercion(nodo_actual.right)
            else:
                self._insert(key, nodo_actual.right)
        else:
            print("¡La key ya esta en el árbol!")

    def toString(self):
        if self.root != None:
            self._to_string(self.root)
            print("{%s}" % self.strArbol[:-2])

    def _to_string(self, nodo_actual):
        if nodo_actual != None:
            self._to_string(nodo_actual.left)
            self.strArbol += '%s, ' % str(nodo_actual.key)
            self._to_string(nodo_actual.right)

    def _inspeccionar_insercion(self, nodo_actual, camino=[]):

        if nodo_actual.father == None:
            return

        camino = [nodo_actual] + camino

        altura_izquierda = self.get_altura(nodo_actual.father.left)
        altura_derecha = self.get_altura(nodo_actual.father.right)

        if abs(altura_izquierda - altura_derecha) > 1:

            camino = [nodo_actual.father] + camino
            self._rebalance_nodo(camino[0], camino[1], camino[2])

            return

        nueva_altura = 1 + nodo_actual.height

        if nueva_altura > nodo_actual.father.height:

            nodo_actual.father.height = nueva_altura

        self._inspeccionar_insercion(nodo_actual.father, camino)


    def _rebalance_nodo(self, z, y, x):

        if y == z.left and x == y.left:
            self._rotar_derecha(z)

        elif y == z.left and x == y.right:
            self._rotar_izquierda(y)
            self._rotar_derecha(z)

        elif y == z.right and x == y.right:
            self._rotar_izquierda(z)

        elif y == z.right and x == y.left:
            self._rotar_derecha(y)
            self._rotar_izquierda(z)

        else:
            raise Exception(
                '_rebalance_nodo: configuración de nodo z, y, x no reconocida!')

    def _rotar_derecha(self, z):
        sub_raiz = z.father
        y = z.left
        t3 = y.right
        y.right = z
        z.father = y
        z.left = t3

        if t3 != None:
            t3.father = z
        y.father = sub_raiz

        if y.father == None:
            self.root = y

        else:
            if y.father.left == z:
                y.father.left = y

            else:
                y.father.right = y
        z.height = 1 + max(self.get_altura(z.left),
                        self.get_altura(z.right))
        y.height = 1 + max(self.get_altura(y.left),
                        self.get_altura(y.right))

    def _rotar_izquierda(self, z):

        sub_raiz = z.father
        y = z.right
        t2 = y.left
        y.left = z
        z.father = y
        z.right = t2

        if t2 != None:
            t2.right = z
        y.father = sub_raiz

        if y.father == None:
            self.root = y

        else:
            if y.father.left == z:
                y.father.left = y

            else:
                y.father.right = y
        z.height = 1 + max(self.get_altura(z.left),
                           self.get_altura(z.right))
        y.height = 1 + max(self.get_altura(y.left),
                           self.get_altura(y.right))
        
    
    def encontrar(self, key):
        if self.root != None:
            return self._encontrar(key, self.root)
        else:
            return None

    def _encontrar(self, key, nodo_actual):
        if key == nodo_actual.key:
            return nodo_actual


    def buscar(self, key):

        if self.root != None:
            return self._buscar(key, self.root)

        else:
            return False

    def _buscar(self, key, nodo_actual):

        if key == nodo_actual.key:
            return True

        elif key < nodo_actual.key and nodo_actual.left != None:
            return self._buscar(key, nodo_actual.left)

        elif key > nodo_actual.key and nodo_actual.right != None:
            return self._buscar(key, nodo_actual.right)
        
        else:
            return False