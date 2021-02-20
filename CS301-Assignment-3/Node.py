
class Node:

    def __init__(self, data, nxt = None):
        self.data = data
        self.nextElt = nxt

    def fetchData(self):
        return self.data

    def fetchNext(self):
        return self.nextElt

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.nextElt = next