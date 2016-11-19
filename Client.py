class Client:

    def __init__(self, ID):
        self.ID = ID
        print( "Client",ID,"Ready")

    def getId(self):
        return self.ID

    def atended(self):
        print ("Client", self.getId(),"was attended.");
