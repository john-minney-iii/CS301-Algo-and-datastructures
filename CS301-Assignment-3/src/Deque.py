
'''
    The Deque is also based off a list so the time complexity of list
    related calls will transfer over. The Deque is also a very quick
    collection.
'''

class Deque:

    def __init__(self):
        self.elements = []

    def addFront(self, elt):            # Constent O(1) since it doesn't have to shift values
        self.elements.append(elt)

    def addRear(self, elt):             # Constent O(1) since it doesn't have to shift values
        self.elements.insert(0, elt)

    def removeFront(self):              # Constent O(1) since it doesn't have to shift values
        return self.elements.pop()

    def removeRear(self):               # Constent O(1) since it doesn't have to shift values
        return self.elements.pop(0)
    
    def isEmpty(self):                  # Constent O(1)
        return not self.elements
    
    def size(self):                     # Constent O(1)
        return len(self.elements)

    def __str__(self):                  # O(n)
        return 'Deque: ' + str(self.elements).strip('[]')

    