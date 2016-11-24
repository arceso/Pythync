import threading
import random
from time import sleep

#Clase que se encarga de ver quien entra y quien sale de la barberia (monitor)

class Barberia(threading.Thread):

    #El constructor pide el número de asientos que puede aceptar
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.__cerradura = threading.Condition()
        self.__numSillas = num
        self.__sillaMaestra = False
        self.__clientesEnEspera = 0
        self.__listaNombres = []

    #Esta función se encarga de hacer un acquire para cortar el pelo al
    #thread cliente que haya entrado antes y después un realese al terminar
    def cortarPelo(self):
        self.__sillaMaestra = True
        self.__clientesEnEspera -= 1
        print("Barbero cortando el pelo...")
        #Tiempo que tarda el barbero en cortar el pelo al cliente
        sleep(random.uniform(.25, 1))
        print("Pelo cortado a " + self.__listaNombres[0])
        self.__listaNombres.remove(self.__listaNombres[0])
        self.__sillaMaestra = False

    #Cambia el estado de la silla principal
    def setSillaOcupada(self, ocupada):
        self.__sillaMaestra = ocupada

    #Devuelve los clientes que están esperando
    def getCuantosClientes(self):
        return self.__clientesEnEspera

    #Devuelve el estado de la silla principal
    def getSillaOcupada(self):
        return self.__sillaMaestra

    #Agrega un cliente en la espera
    def agregarCliente(self):
        if self.__clientesEnEspera <= self.__numSillas:
            self.__clientesEnEspera += 1

    #Devuelve la condición de este thread
    def getHilo(self):
        return self.__cerradura

    #Devuelve la lista de nombres que están en la cola de espera
    def getListaNombres(self):
        return self.__listaNombres

    #Sirve para modificar la lista de nombres en espera
    def setListaNombres(self, nombres):
        self.__listaNombres = nombres
