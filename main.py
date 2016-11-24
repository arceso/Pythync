import threading
import random
from modulos.barberia import Barberia
from modulos.cliente import Cliente
from modulos.barbero import Barbero
from time import sleep
from colorama import init, Fore, Back, Style

#El main simplemente tiene lo básico para iniciar las demás clases

def main():
    '''
    Este init es del paquete colorama (sirve para tener colores en las terminales)
    Sirve para inicializar sus variables internas (para que sepa en que entorno
    se encuentra).
    '''
    init()

    '''
    Asi es como se declaran variables globales para que todas las funciones
    puedan utilizarlas.
    '''
    global barberia, barbero, numeroSillas

    #Numero de sillas disponibles para esperar, si sobrepasa no se aceptan más clientes
    numeroSillas = random.randrange(1, 5)

    print(Back.BLUE + "El máximo de clientes es: ", numeroSillas, ".")
    print(Style.RESET_ALL)

    #Instanciamos las clases barberia y barbero
    #Barberia recibe el numero de asientos disponibles
    barberia = Barberia(numeroSillas)

    #Barbero recibe el la clase Barberia
    barbero = Barbero(barberia)

    #Iniciamos los hilos
    barberia.start()
    barbero.start()

    '''
    Este es un inicio de un thread de manera anónima
    Target es la función que se usará como hilo
    Thread también acepta un parámetro más para ponerle un nombre al hilo
    '''
    threading.Thread(target=iniciar, name="Clientes Potenciales").start()

#Esta función sirve para crear una cantidad de clientes (según el while)
def iniciar():
    global barberia, barbero, numeroSillas
    while(True):
        #Mandamos a dormir el bucle para que la creación de clientes tenga algo de tiempo
        sleep(random.uniform(1, 1.5))
        cliente = Cliente(barberia, barbero)
        cliente.setName("Cliente " + cliente.getName())
        #Si hay sitio en la barberia se crea un nuevo proceso que esperará a poder cortarse el pelo
        #sino se perderá ese cliente
        if barberia.getCuantosClientes() < numeroSillas:
            #El cliente estará constantemente viendo si puede o no entrar a la silla principal
            print(Back.YELLOW + "Ha llegado el ", cliente.getName(), ".")
            print(Style.RESET_ALL)
            cliente.start()

        else:
            print(Back.RED + cliente.getName() + "se fue por no tener sitio.")
            print(Style.RESET_ALL)


#Es una forma de decirle a python que la función main() será la principal
if __name__ == "__main__":
    main()
