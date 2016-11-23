import threading
import time
from Client import *

class Barber:

    def __init__(self):
        print("Barber Ready!")
        self.lock = threading.Lock()
        sleepingChair = threading.Condition()
        threading.Thread(name="sleeper", target=self.goToSeleep, args=(sleepingChair,)).start()
        threading.Thread(name="wakeup", target=self.wakeUp, args=(sleepingChair,)).start()

    def attend(self, client):
        with self.lock:
            print("Client",client.getId() ,"being attended!")
            client.atended()

    def  goToSeleep(self, cv):
        print("I'm sleeping!")
        with cv:
            cv.wait()
            print("ASD")

    def  wakeUp(self, cv):
        print("I'm awake!")
        with cv:
            cv.notifyAll()

#Ej:
#Barber().attend(Client(7))
