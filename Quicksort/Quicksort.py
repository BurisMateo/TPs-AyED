#Buris Mateo - Nuñez Matias

#import random

def QuicksortRe(lista,inf,sup):
    if (inf<sup):
        I=inf
        J=sup
        pivot=lista[inf]
        while (I<J):
            while (lista[I]<=pivot) and (I<J):
                I+=1
            while (lista[J]>pivot):
                J-=1
            if (I<J):
                (lista[I],lista[J])=(lista[J],lista[I])
        (lista[inf],lista[J])=(lista[J],lista[inf])
        QuicksortRe(lista,inf,J-1)
        QuicksortRe(lista,J+1,sup)

def QuicksortIt(A, inf, sup):
    pila = []
    pila.append((inf,sup))
    while pila:
        pos = pila.pop()
        sup, inf = pos[1], pos[0]
        piv = particion(A,inf,sup)
        if piv-1 > inf:
            pila.append((inf,piv-1))
        if piv+1 < sup:
            pila.append((piv+1,sup))

def particion(A, inf, sup):
    piv = A[inf]
    i = inf + 1
    j = sup
    while 1:
        while i <= j  and A[i] <= piv:
            i +=1
        while j >= i and A[j] >= piv:
            j -=1
        if j <= i:
            break
        A[i], A[j] = A[j], A[i]
    A[inf], A[j] = A[j], A[inf]
    return j

def bb(Pri,Ult,lista,Kx):
    pos = -1
    if (Pri<=Ult):
        M=(Pri+Ult)//2    
        if (lista[M]==Kx):
            pos = M
        else:
            if (lista[M]>Kx):                               
                pos = bb(Pri,M-1,lista,Kx)
            else:
                pos = bb(M+1,Ult,lista,Kx)
    return pos


"""
def nRandom(L, cantidad):
    while len(L)<cantidad:
        num = random.randint(0,20)
        if (num not in L):
            L.append(num)

lista = []
nRandom(lista,10)
print(lista)
QuicksortRe(lista,0,len(lista)-1)
print(lista)
"""