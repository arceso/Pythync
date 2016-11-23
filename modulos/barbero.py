import threading

class Barbero(threading.Thread):
    def __init__(self, monitor):
        threading.Thread.__init__(self)
        self.__cerradura = threading.Condition()
        self.__duerme = False
        self.__barberia = monitor

    def run(self):
        while(True):
            if not self.__barberia.getSillaOcupada() and self.__barberia.getCuantosClientes() == 0 and not self.__duerme:
                self.dormir()

    def dormir(self):
        print("Barbero se puso a dormir")
        self.__duerme = True
        self.__barberia.setSillaOcupada(True)
        '''
        try:
            self.__cerradura.acquire()
            print("Cerradura cerrada")
            self.__cerradura.wait()
        finally:
            print("Cerradura abierta")
            self.__cerradura.release()
        '''
        with self.__cerradura:
            self.__cerradura.wait()
        self.__duerme = False
        self.__barberia.setSillaOcupada(False)

    def getEstado(self):
        return self.__duerme

    def getHilo(self):
        return self.__cerradura
