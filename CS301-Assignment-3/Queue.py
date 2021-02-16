
'''
    TODO: In comments, describe the running time of each method
          of your implementation.
'''

class Queue:

    def __init__(self):
        self.elements = []

    def enqueue(self, elt):
        self.elements.insert(0, elt)

    def dequeue(self):
        return self.elements.pop()

    def isEmpty(self):
        return not self.elements

    def size(self):
        return len(self.elements)
    
    def __str__(self):
        return 'Queue: ' + str(self.elements).strip('[]')