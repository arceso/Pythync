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

def doTheWorkday():
    print("Barbery is OPEN!")

    sleepingChair = threading.Event()
    barber = Barber(sleepingChair)
    clientsOutside = genClientArray(MAXCLIENTSOUTSIDE)
    clientsInside = LinkedList(MAXCLIENTSINSIDE)

    for clientOutside in clientsOutside: clientOutside.tryToJoin(clientsInside)

    while (clientsLeft()):
        time.sleep(1)

        if(clientsInside.isEmpty): barber.goToSeleep()
        else:
         barber.wakeUp()
         barber.attend(clientsInside.pop())



#    while(not clientsInside.isEmpty()): barber.attend( clientsInside.pop())

    print("Barbery is CLOSED!")

def checkForSeat(client):
    if (not clientsInside.isFull()): clientsInside.push(client)

def wakeUpBarber(sleepingChair):
    sleepingChair.set()
    
#doTheWorkday()
