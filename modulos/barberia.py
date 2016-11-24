import threading
import random
from time import sleep

class Barberia(threading.Thread):

    def __init__(self, num):
        threading.Thread.__init__(self)
        self.__cerradura = threading.Condition()
        self.__numSillas = num
        self.__sillaMaestra = False
        self.__clientesEnEspera = 0
        self.__listaNombres = []

    def run(self):
        while(True):
            pass

    def cortarPelo(self):
        with self.__cerradura:
            self.__sillaMaestra = True
            self.__clientesEnEspera -= 1
            print("Barbero cortando el pelo...")
            sleep(random.uniform(.25, 1))
            print("Pelo cortado a " + self.__listaNombres[0])
            self.__listaNombres.remove(self.__listaNombres[0])
            self.__sillaMaestra = False

    def setSillaOcupada(self, ocupada):
        self.__sillaMaestra = ocupada

    def getCuantosClientes(self):
        return self.__clientesEnEspera

    def getSillaOcupada(self):
        return self.__sillaMaestra

    def agregarCliente(self):
        if self.__clientesEnEspera <= self.__numSillas:
            self.__clientesEnEspera += 1

    def getHilo(self):
        return self.__cerradura

    def getListaNombres(self):
        return self.__listaNombres

    def setListaNombres(self, nombres):
        self.__listaNombres = nombres
