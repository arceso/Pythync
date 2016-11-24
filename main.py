import threading
import random
from modulos.barberia import Barberia
from modulos.cliente import Cliente
from modulos.barbero import Barbero
from time import sleep

def main():
    '''
    Asi es como se declaran variables globales para que todas las funciones
    puedan utilizarlas.
    '''
    global barberia, barbero, numeroSillas

    #Numero de sillas disponibles para esperar, si sobrepasa no se aceptan más clientes
    numeroSillas = random.randrange(1, 5)

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
        sleep(random.uniform(.25, .5))

        if barberia.getCuantosClientes() < numeroSillas:
            cliente = Cliente(barberia, barbero)
            cliente.setName("Cliente " + cliente.getName())
            cliente.start()
        else:
            print("Un cliente se fue por no tener sitio.")

if __name__ == "__main__":
    main()
