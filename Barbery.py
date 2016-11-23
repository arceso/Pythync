from Client import *
from Barber import *
from SeatQueue import *

import time

MAXCLIENTSOUTSIDE = 10
MAXCLIENTSINSIDE = 3

def genClientArray(size):
    clients = []
    for index in range(size): clients.append( Client(index))
    return clients

def clientQueue(size):
    clients = LinkedList()
    for index in range(0, size): clients.push( Node( Client( index)))
    return clients


def checkForSeat(client):
    if (not clientsInside.isFull()): clientsInside.push(client)

def wakeUpBarber(sleepingChair):
    sleepingChair.set()


#Not tested
def haveClientsLeft():
    return ClientsInside.isEmpty and clientsOutside.size != 0


if __name__ == "__main__":
    print("Barbery is OPEN!")

    clientsOutside = genClientArray(MAXCLIENTSOUTSIDE)
    while(not clientsOutside.isEmpty)
        time.
        clientsInside = LinkedList(MAXCLIENTSINSIDE)

        for clientOutside in clientsOutside: clientOutside.tryToJoin(clientsInside)

        while (haveClientsLeft()):





        #    while(not clientsInside.isEmpty()): barber.attend( clientsInside.pop())

        print("Barbery is CLOSED!")
