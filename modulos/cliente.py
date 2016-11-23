import threading

class Cliente(threading.Thread):

    def __init__(self, monitor, barbero):
        threading.Thread.__init__(self)
        self.__barberia = monitor
        self.__barbero = barbero
        self.__barberia.agregarCliente()
        print("Hay ", self.__barberia.getCuantosClientes(), " clientes en espera")

    def run(self):
        if self.__barbero.getEstado():
            self.despertar()
        while(True):
            if not self.__barberia.getSillaOcupada():
                self.__barberia.cortarPelo()
                break

    def despertar(self):
        print("Despertando al barbero")
        '''
        try:
            self.__barbero.getHilo().acquire()
            self.__barbero.getHilo().notify_all()
        finally:
            sself.__barbero.getHilo().release()
        '''
        with self.__barbero.getHilo():
            self.__barbero.getHilo().notify()
