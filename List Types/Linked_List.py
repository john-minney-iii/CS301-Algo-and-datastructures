from Node import Node

'''
    Since the linked list is an abstract data structure and
    is showing how lists work where we don't useually see it.
    Though this linked list may be working, that doesn't mean it
    is running as quick as it could be.

    For the big o notation let n be the size of the linked-list

'''

class Linked_List:

    def __init__(self):
        self.head = None

    # -------------------------------------------
    # Constent O(1)
    def add(self, item): 
        self.head = Node(item, self.head)

    # -------------------------------------------
    # If the item is first O(1)
    # Otherwise O(n)
    def remove(self, item):
        currElt = self.head
        if currElt.fetchData() == item:
            self.head = currElt.fetchNext()
            return
        
        while currElt: # Loops through all the elements
            if currElt.fetchData() == item:
                break
            prevElt = currElt
            currElt = currElt.fetchNext()

        if not currElt:
            raise Exception('Element Not Found.')
            return
        
        prevElt.setNext(currElt.fetchNext())
        currElt = None

    # -------------------------------------------
    # O(n)
    def search(self, item) -> bool:
        return self._search_helper(item)[0]
    
    '''
    Returns if value is found and its position
    '''
    def _search_helper(self, item):
        currentElt = self.head
        count = 0
        while currentElt != None: # Loops through all the elements
            if currentElt.fetchData() == item:
                return True, count
            currentElt = currentElt.fetchNext()
            count += 1

        return False, 0

    # -------------------------------------------
    # O(1)
    def isEmpty(self) -> bool:
        return self.head is None

    # -------------------------------------------
    # O(n)
    def size(self) -> int:
        currentElt = self.head
        count = 0

        while currentElt != None: # Loops through all the elements
            count += 1
            currentElt = currentElt.fetchNext()
        return count

    # -------------------------------------------
    # O(n)
    def append(self, item):
        currElt = self.head
        if currElt:
            while currElt.fetchNext(): # Loops through all the elements
                currElt = currElt.fetchNext()
            currElt.setNext(Node(item))
        else:
            self.add(item)

    # -------------------------------------------
    # O(n)
    # This also uses the _search_helper method
    def index(self, item) -> int:
        return self._search_helper(item)[1]

    # -------------------------------------------
    # If first element: O(1)
    # Otherwise O(n)
    def insert(self, pos, item):
        if pos > self.size() - 1 : raise IndexError("list index out of range")
        elif pos == 0 : self.add(item)
        else:
            currElt = self.head
            count = 0
            newNode = Node(item)
            while currElt: # Loops through all the elements
                prevElt = currElt
                currElt = currElt.fetchNext()
                count += 1
                if count == pos:
                    prevElt.setNext(newNode)
                    newNode.setNext(currElt)

    # -------------------------------------------
    # Both last element and index take O(n)
    def pop(self, pos = -1) -> str:
        if pos == -1:
            return self._pop_last()
        else:
            return self._pop_pos(pos)
    
    def _pop_last(self) -> str:
        currElt = self.head
        while currElt.fetchNext(): # Loops through all the elements
            if currElt.fetchNext().fetchNext() == None:
                data = currElt.fetchNext().fetchData()
                currElt.setNext(None)
                return data
            else:
                currElt = currElt.fetchNext()

    def _pop_pos(self, pos) -> str:
        if pos > self.size() - 1 : raise IndexError("list index out of range")
        elif pos == 0 : 
            data = self.head.fetchData()
            self.remove(data)
            return data
        else:
            currElt = self.head
            count = 0
            while currElt: # Loops through all the elements
                prevElt = currElt
                currElt = currElt.fetchNext()
                count += 1
                if count == pos:
                    data = currElt.fetchData()
                    prevElt.setNext(currElt.fetchNext())
                    currElt = None
                    return data

    # -------------------------------------------
    # O(n)
    def printList(self): 
        temp = self.head 
        print('Linked List:')
        while(temp): # Loops through all the elements
            print (" %d" %(temp.fetchData()), end=''), 
            temp = temp.fetchNext()
        print('\n')