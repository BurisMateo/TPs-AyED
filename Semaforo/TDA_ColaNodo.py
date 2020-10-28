#Buris Mateo - Nuñez Matias

class NodoCola():
    def __init__(self):
        self.info= None
        self.sig= None

class T_Cola():
    def __init__(self):
        self.tamanio = 0
        self.frente = None
        self.final = None

    def encolar(self,x):
        aux = NodoCola()
        aux.info = x
        aux.sig = None
        if (self.final==None):
            self.frente=aux
        else:
            self.final.sig=aux
        self.final=aux
        self.tamanio=self.tamanio+1

    def desencolar(self):
        aux = self.frente
        self.frente = aux.sig
        if (self.frente==None):
            self.final = None
        self.tamanio = self.tamanio-1

    def colavacia(self):
        if self.tamanio == 0:
            return True
        else:
            return False

"""
cola = T_Cola()

for i in range(1, 6):
    encolar(cola, str(i))

aux = cola.frente
for i in range(cola.tamanio):
    print(aux.info)
    aux = aux.sig

desencolar(cola)
desencolar(cola)
print('')
aux = cola.frente
for i in range(cola.tamanio):
    print(aux.info)
    aux = aux.sig
"""