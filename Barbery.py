import Barber
import Client
import SeatQueue

print("Barbery is OPEN!")

clients = LinkedList()
barber = Barber()

TOTALCLIENTS = 3


for index in range(0, TOTALCLIENTS): clients.push(Client(index))

for index in range(0, TOTALCLIENTS): barber.attend(Client(index))

for index in range(0, TOTALCLIENTS): clients.pop()

raw_input('Enter your input:')

print("Barbery is CLOSED!")
