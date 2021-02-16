#Buris Mateo - Nuñez Matias

max=100
class T_Pila(object):
    def __init__(self):
        self.tope=-1
        self.dato=[]
        for I in range (0,max):
            self.dato.append(0)

def apilar(p,x):
    p.tope = p.tope + 1
    p.dato[p.tope] = x
    
def desapilar(p):
    x=p.dato[p.tope]
    p.tope=p.tope-1
    return x
    
def pilaLlena(p):
    return p.tope == max-1

def pilaVacia(p):
    return p.tope == -1

def tamanio(p):
    return p.tope + 1    

def barrido(p):
    paux = T_Pila()
    while(not pilaVacia(p)):
        x=desapilar(p)        
        print(x)
        apilar(paux,x)
        
    while(not pilaVacia(paux)):
        x=desapilar(paux)        
        apilar(p,x)


"""
pila = T_Pila()
apilar(pila, 1)
apilar(pila, 2)
apilar(pila, 3)
barrido(pila)
barrido(pila)
"""