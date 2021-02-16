
'''
    TODO: In comments, describe the running time of each method
          of your implementation.
'''

class Stack:

    def __init__(self):
        self.elements = []

    def push(self, elt):
        self.elements.append(elt)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def isEmpty(self):
        return not self.elements
    
    def size(self):
        return len(self.elements)

    def __str__(self):
        return 'Stack: ' + str(self.elements[::-1]).strip('[]')