import threading

#Clase que despierta al barbero si está dormido

class Cliente(threading.Thread):

    #El constructor pide un monitor en este caso barberia y una clase barbero
    #Obtiene las condiciones de barberia
    def __init__(self, barberia, barbero):
        threading.Thread.__init__(self)
        self.__barberia = barberia
        self.__barbero = barbero
        self.__barberia.agregarCliente()
        self.__cerradura = self.__barberia.getHilo()
        self.__listaNombres = self.__barberia.getListaNombres()
        print("Hay ", self.__barberia.getCuantosClientes(), " clientes en espera")

    #En esta función se ve si el barbero está dormido y después se entra en un
    #bucle para intentar entrar en la silla principal para que le corten el pelo
    def run(self):
        if self.__barbero.getEstado():
            self.despertar()
        while(True):
            if not self.__barberia.getSillaOcupada():
                self.__listaNombres.append(self.getName())
                self.__barberia.setListaNombres(self.__listaNombres)
                self.__barberia.cortarPelo()
                break

    #Esta función solo será llamado cuando el barbero esté durmiendo y le despertará
    #con la condición notify
    def despertar(self):
        print("Despertando al barbero")
        with self.__cerradura:
            self.__cerradura.notify()
