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

    def run(self):
        while(True):
            pass

    def cortarPelo(self):
        with self.__cerradura:
            self.__sillaMaestra = True
            self.__clientesEnEspera -= 1
            print("Barbero cortando el pelo...")
            sleep(random.uniform(1, 5))
            print("Pelo cortado a ", self.__cortandoAlHilo)
            self.__sillaMaestra = False

    def setSillaOcupada(self, ocupada):
        self.__sillaMaestra = ocupada

    def getCuantosClientes(self):
        return self.__clientesEnEspera

    def getSillaOcupada(self):
        return self.__sillaMaestra

    def agregarCliente(self):
        self.__clientesEnEspera += 1

    def getHilo(self):
        return self.__cerradura

    def setNombreHiloActual(self, nombre):
        self.__cortandoAlHilo = nombre
