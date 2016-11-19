class Client:

    def __init__(self, ID):
        self.ID = ID
        print "Client %d Ready" % (ID)

    def getId(self):
        return self.ID

    def atended(self):
        print "Client %d was attended." % (self.getId());
