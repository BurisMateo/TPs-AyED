#Buris Mateo - Nuñez Matias

import sys
import time
from TDA_ColaNodo import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTimeEdit
from PyQt5.QtGui import QPixmap 
from PyQt5 import uic
from PyQt5.QtTest import QTest

class Semaforo():
    def __init__(self, id):
        self.id = id
        self.color = 'rojo'
        self.cola = T_Cola()

class MainWindow (QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("semaforo.ui", self)
        self.estado = True
        pixmap = QPixmap('fondo.jpg')
        self.fondoi.setPixmap(pixmap)
        self.go.clicked.connect(self.iniciar)
        self.stop.clicked.connect(self.detener)

    def iniciar(self):
        self.estado = True
        pixmap = QPixmap('rojo.png')
        self.sema1i.setPixmap(pixmap)
        self.sema2i.setPixmap(pixmap)
        self.sema3i.setPixmap(pixmap)
        self.sema4i.setPixmap(pixmap)
        sema1 = Semaforo("1")
        sema1.cola.encolar("auto")
        sema2 = Semaforo("2")
        sema2.cola.encolar("auto")
        sema3 = Semaforo("3")
        sema3.cola.encolar("auto")
        sema4 = Semaforo("4")
        sema4.cola.encolar("auto")
        self.ciclo(sema1, sema2, sema3, sema4)

    def detener(self):
        self.estado = False

    def cambiar_color(self, object):
        if (object.color == "rojo"):
            object.color = "verde"
            pixmap = QPixmap('verde.png')
            object.cola.desencolar()
        else:
            object.color = "rojo"
            pixmap = QPixmap('rojo.png')
            object.cola.encolar("auto")
        return pixmap

    def set_color (self, object):
        if (object.id == "1"):
            pixmap = self.cambiar_color(object)
            self.sema1i.setPixmap(pixmap)
        elif (object.id == "2"):
            pixmap = self.cambiar_color(object)
            self.sema2i.setPixmap(pixmap)
        elif (object.id == "3"):
            pixmap = self.cambiar_color(object)
            self.sema3i.setPixmap(pixmap)
        elif (object.id == "4"):
            pixmap = self.cambiar_color(object)
            self.sema4i.setPixmap(pixmap)
 
    def ciclo (self, sema1, sema2, sema3, sema4):
        i=1
        
        while self.estado==True:
            if sema1.id == str(i):
                self.set_color(sema1)
                QTest.qWait(2000)
                self.set_color(sema1)
            if sema2.id == str(i):
                self.set_color(sema2)
                QTest.qWait(2000)
                self.set_color(sema2)
            if sema3.id == str(i):
                self.set_color(sema3)
                QTest.qWait(2000)
                self.set_color(sema3)
            if sema4.id == str(i):
                self.set_color(sema4)
                QTest.qWait(2000)
                self.set_color(sema4)
            i+=1
            if i==5:
                i=1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
