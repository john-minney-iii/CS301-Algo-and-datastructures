
'''
    For the most part the Stack is an extreamly quick collection.
    Since the Stack is basically just a list the time complexity of the list
    transfers over.
'''

class Stack:

    def __init__(self):             # Constent Method O(1)
        self.elements = []

    def push(self, elt):
        self.elements.append(elt)   # Constent Method O(1) -> This is just a list append which we proved in assignment 2 is constent

    def pop(self):
        return self.elements.pop()  # Constenet Method O(1) -> This was proven in assignment 2

    def peek(self):
        return self.elements[-1]    # Because it is only finding the last element this will be constent shince it doesn't have to iterate O(1)

    def isEmpty(self):
        return not self.elements    # Constent O(1)
    
    def size(self):
        return len(self.elements)   # Constent O(1)

    def __str__(self):              # O(n) since it has to iterate to print all the elements
        return 'Stack: ' + str(self.elements[::-1]).strip('[]') 