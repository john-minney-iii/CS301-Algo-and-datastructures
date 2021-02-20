
class Node:

    def __init__(self, data, nxt = None, dbly = False):
        self.dbly = dbly
        self.data = data
        self.nextElt = nxt
        self.prev = None

    def fetchData(self):
        return self.data

    def fetchNext(self):
        return self.nextElt

    def fetchPrev(self):
        if self.dbly: return self.prev

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.nextElt = next

    def setPrev(self, prev):
        if self.dbly: self.prev = prev