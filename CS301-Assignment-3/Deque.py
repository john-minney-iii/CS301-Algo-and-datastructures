
'''
    TODO: In comments, describe the running time of each method
          of your implementation.
'''

class Deque:

    def __init__(self):
        self.elements = []

    def addFront(self, elt):
        self.elements.append(elt)

    def addRear(self, elt):
        self.elements.insert(0, elt)

    def removeFront(self):
        return self.elements.pop()

    def removeRear(self):
        return self.elements.pop(0)
    
    def isEmpty(self):
        return not self.elements
    
    def size(self):
        return len(self.elements)

    def __str__(self):
        return 'Deque: ' + str(self.elements).strip('[]')

    