
'''
    Since a Queue and a Deque are practically the same thing their
    running times are going to be identical
'''

class Queue:

    def __init__(self):
        self.elements = []

    def enqueue(self, elt):              # Constent O(1) since it doesn't have to shift values
        self.elements.insert(0, elt)

    def dequeue(self):                   # Constent O(1) since it doesn't have to shift values
        return self.elements.pop()

    def isEmpty(self):                   # Constent O(1)
        return not self.elements

    def size(self):                      # Constent O(1)
        return len(self.elements)
    
    def __str__(self):                  # O(n)
        return 'Queue: ' + str(self.elements).strip('[]')