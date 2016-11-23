import threading

class Cliente(threading.Thread):

    def __init__(self, barberia, barbero):
        threading.Thread.__init__(self)
        self.__barberia = barberia
        self.__barbero = barbero
        self.__barberia.agregarCliente()
        self.__cerradura = barberia.getHilo()
        print("Hay ", self.__barberia.getCuantosClientes(), " clientes en espera")

    def run(self):
        if self.__barbero.getEstado():
            self.despertar()
        while(True):
            if not self.__barberia.getSillaOcupada():
                self.__barberia.setNombreHiloActual(self.getName())
                self.__barberia.cortarPelo()
                break

    def despertar(self):
        print("Despertando al barbero")
        with self.__cerradura:
            self.__cerradura.notify()
