class Node(object):

    def __init__(self, client = None, next = None):
        self.client = client
        self.next = next

    def __str__(self):
        return str(self.client)


class LinkedList(object):

    def __init__(self):
        self.init = Node()
        print("LinkedList Ready")

    def pop(self):
        first = self.init.next
        self.init.next = first.next
        return first

    def push(self, node):
        nodeIterator = self.init
        while(nodeIterator.next != None): nodeIterator = nodeIterator.next
        nodeIterator.next = node

    def showList(self):
        nodeIterator = self.init
        i = 0
        while(nodeIterator.next != None): print "Node no%d: %d" % (++i, nodeIterator = nodeIterator.next)
