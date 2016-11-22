class Node(object):

    def __init__(self, client = None, nextClient = None):
        self.client = client
        self.nextClient = nextClient

    def __str__(self):
        return str(self.client)


class LinkedList(object):

    def __init__(self, MAX):
        self.init = Node()
        self.MAX = MAX
        print("Queue Ready")


    def pop(self):
        first = self.init.nextClient
        self.init.nextClient = first.nextClient
        return first.client

    def push(self, node):
        nodeIterator = self.init
        while(nodeIterator.nextClient != None): nodeIterator = nodeIterator.nextClient
        nodeIterator.nextClient = node

    def showList(self):
        nodeIterator = self.init
        i = 0
        while(nodeIterator.nextClient != None):
            nodeIterator = nodeIterator.nextClient
            print ("Node no", ++i, nodeIterator)

    def isEmpty(self):
        return self.init.nextClient == None

    def isFull(self):
        nodeIterator = self.init
        while(nodeIterator.nextClient != None):
            nodeIterator = nodeIterator.nextClient
            cont += 1
            if (cont == MAX) return True
        return False
