import threading

class Barber(threading.Thread):

    lock = threading.Lock()


    def __init__(self, sleepingChair):
        print("Barber Ready!")
        threading.Thread.__init__(self)
        self.sleepingChair = sleepingChair

    def attend(self, client):
        with lock:
            print("Client",client.getId() ,"being attended!")
            client.atended()

    def  goToSeleep(self):
        print("I'm sleeping!")
        while(self.sleepingChair.wait()): print("awake!")

    def  wakeUp(self):
        print("I'm awake!")
        self.sleepingChair.set()


sleepingChair = threading.Event()
b = Barber(sleepingChair)
b.daemon = True
b.start()
print(1)
b.goToSeleep()
print(2)
sleepingChair.set()
print(3)
