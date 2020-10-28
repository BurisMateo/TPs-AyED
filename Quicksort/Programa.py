#Buris Mateo - Nuñez Matias

import sys
import random
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from Quicksort import *

class Programa(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("/home/mateo/Escritorio/TPs Python/Entregar/Quicksort/Programa.ui", self)
        self.lista = []
        self.Generar.clicked.connect(self.generar_lista)
        self.Ordenar_Re.clicked.connect(self.ordenar_recursivo)
        self.Ordenar_It.clicked.connect(self.ordenar_iterativo)
        self.Buscar.clicked.connect(self.busqueda)
        self.show()

    def generar_lista(self):
        c=15
        n=10
        x=''
        self.lista = []
        while len(self.lista)<c:
            num = random.randint(0,50)
            if (num not in self.lista):
                self.lista.append(num)
        for i in range (c):
            x += str(self.lista[i])+' '
        self.listarandom.append("[ "+x+"]")
        return self.lista
    
    def ordenar_recursivo(self):
        c=15
        x=''
        QuicksortRe(self.lista,0,len(self.lista)-1)
        for i in range (c):
            x += str(self.lista[i])+' '
        self.listarecursiva.append("[ "+x+"]")
    
    def ordenar_iterativo(self):
        c=15
        x=''
        QuicksortIt(self.lista,0,len(self.lista)-1)
        for i in range (c):
            x += str(self.lista[i])+' '
        self.listaiterativa.append("[ "+x+"]")
    
    def busqueda(self):
        pos=None
        bus = self.buscado.text()
        try:
            pos = bb(0,len(self.lista)-1,self.lista,int(bus))
            if (pos!=-1):
                self.resultadoBB.append("el numero "+bus+" se encuentra en la posicion "+str(pos+1))
            else:
                self.resultadoBB.append("el numero "+bus+" no se encuentra en la lista")
        except ValueError:
            self.resultadoBB.append("debe ingresar un numero para buscarlo")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Programa()
    sys.exit(app.exec_())