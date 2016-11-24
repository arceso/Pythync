import threading
from colorama import init, Fore, Back, Style

#Barbero es la clase que acepta hilos si está despierto pero solo acepta a 1 a la vez

#Se inicia barbero(threading.Thread) es como un extends de java
class Barbero(threading.Thread):

    #El constructor pide el monitor (barberia)
    #Y las condiciones
    def __init__(self, barberia):
        threading.Thread.__init__(self)
        self.__duerme = False
        self.__barberia = barberia
        self.__cerradura = barberia.getHilo()

    #Este método se inicia cuando se instancia la clase barbero
    #Lo único que hace es ver si la silla no está ocupada, no hay nadie a la esperar
    #y si está despierto sino vuelve a dormir al thread
    def run(self):
        while(True):
            with self.__cerradura:
                if not self.__barberia.getSillaOcupada() and self.__barberia.getCuantosClientes() == 0 and not self.__duerme:
                    self.dormir()

    #Esta función es la que hace dormir al thread con wait(), es necesario el with
    #porque recibe el self.__cerradura que contiene los acquire y release
    #es decir, con with hace ambas cosas si se pasa threading.Condition()
    def dormir(self):
        with self.__cerradura:
            self.__duerme = True
            self.__barberia.setSillaOcupada(True)
            print(Back.MAGENTA + "Barbero se puso a dormir")
            print(Style.RESET_ALL)
            self.__cerradura.wait()
        self.__duerme = False
        self.__barberia.setSillaOcupada(False)

    def getEstado(self):
        return self.__duerme
