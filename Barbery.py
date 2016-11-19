from Client import *
from Barber import *
from SeatQueue import *


def genClientArray(size):
    clients = LinkedList()
    for index in range(0, size): clients.push( Node( Client( index)))
    return clients

def doTheWorkday():
    print("Barbery is OPEN!")

    barber = Barber()

    clients = genClientArray(TOTALCLIENTS)
    while(not clients.isEmpty()): barber.attend( clients.pop())

    print("Barbery is CLOSED!")

doTheWorkday()
