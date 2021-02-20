from Node import Node

'''
    TODO: In comments, describe the running time of each method
          of your implementation.
'''

class Doubly_Linked:

    def __init__(self):
        self.head = None

    # -------------------------------------------

    def add(self, item):
        if self.head is None:
            self.head = Node(data=item, dbly=True)
        else:
            new = Node(data=item, dbly=True)
            new.setNext(self.head)
            self.head.setPrev(new)
            self.head = new

    # -------------------------------------------

    #TODO: Create remove(item):
    def remove(self, item):
        currElt = self.head
        if currElt.fetchData() == item:
            self.head = currElt.fetchNext()
            return
        
        while currElt:
            if currElt.fetchData() == item:
                break
            prevElt = currElt
            currElt = currElt.fetchNext()
            nextElt = currElt.fetchNext()

        if not currElt:
            raise Exception('Element Not Found.')
            return
        
        prevElt.setNext(currElt.fetchNext())
        if nextElt != None : nextElt.setPrev(prevElt)
        currElt = None

    # -------------------------------------------

    def search(self, item) -> bool:
        return self._search_helper(item)[0]
    
    '''
    Returns if value is found and its position
    '''
    def _search_helper(self, item):
        currentElt = self.head
        count = 0
        while currentElt != None:
            if currentElt.fetchData() == item:
                return True, count
            currentElt = currentElt.fetchNext()
            count += 1

        return False, 0

    # -------------------------------------------

    def isEmpty(self) -> bool:
        return self.head is None

    # -------------------------------------------

    def size(self) -> int:
        currentElt = self.head
        count = 0

        while currentElt != None:
            count += 1
            currentElt = currentElt.fetchNext()
        return count

    # -------------------------------------------

    def append(self, item):
        if self.head is None:
            self.head = Node(data=item, dbly=True)
        else:
            currNode = self.head
            while currNode.fetchNext() != None:
                currNode = currNode.fetchNext()
            new = Node(data=item, dbly=True)
            currNode.setNext(new)
            new.setPrev(currNode)

    # -------------------------------------------

    def index(self, item) -> int:
        return self._search_helper(item)[1]

    # -------------------------------------------

    def insert(self, pos, item):
        if pos > self.size() - 1 : raise IndexError("list index out of range")
        elif pos == 0 : self.add(item)
        else:
            currElt = self.head
            count = 0
            newNode = Node(data=item, dbly=True)
            while currElt:
                prevElt = currElt
                currElt = currElt.fetchNext()
                if currElt.fetchNext() != None : nextElt = currElt.fetchNext()
                count += 1
                if count == pos:
                    prevElt.setNext(newNode)
                    newNode.setNext(currElt)
                    if nextElt != None: nextElt.setPrev(prevElt)
                    break

    # -------------------------------------------

    def pop(self, pos = -1) -> str:
        if pos == -1:
            return self._pop_last()
        else:
            return self._pop_pos(pos)

    def _pop_last(self) -> str:
        currElt = self.head
        while currElt.fetchNext():
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
            while currElt:
                prevElt = currElt
                currElt = currElt.fetchNext()
                nextElt = currElt.fetchNext()
                count += 1
                if count == pos:
                    data = currElt.fetchData()
                    prevElt.setNext(currElt.nextElt)
                    if nextElt != None : nextElt.setPrev(prevElt)
                    currElt = None
                    return data

    # -------------------------------------------

    def printList(self): 
        temp = self.head 
        print('Doubly List:')
        while(temp): 
            print (" %d" %(temp.fetchData()), end=''), 
            temp = temp.fetchNext()
        print('\n')