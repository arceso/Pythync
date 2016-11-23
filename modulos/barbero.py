import threading

class Barbero(threading.Thread):
    def __init__(self, barberia):
        threading.Thread.__init__(self)
        self.__duerme = False
        self.__barberia = barberia
        self.__cerradura = barberia.getHilo()

    def run(self):
        while(True):
            with self.__cerradura:
                if not self.__barberia.getSillaOcupada() and self.__barberia.getCuantosClientes() == 0 and not self.__duerme:
                    self.dormir()

    def dormir(self):
        self.__duerme = True
        self.__barberia.setSillaOcupada(True)
        print("Barbero se puso a dormir")
        with self.__cerradura:
            self.__cerradura.wait()
        self.__duerme = False
        self.__barberia.setSillaOcupada(False)

    def getEstado(self):
        return self.__duerme
