from Stack import Stack
from Queue import Queue
from Deque import Deque
from Linked_List import Linked_List
from Doubly_linked import Doubly_Linked

# Analysis Questions
'''
    6. Do you think that python's internal representation 
    of a list is a linked-list, a doubly-linked list or something else? 
    Why or why not? Insert a comment in your code to explain your 
    thinking about this.

    - Personally I don't believe a Python list is any of these data-types. Eventhough
      the Python list runs similarly to a doubly linked list their runtimes are different.
      For example, when you want to access an element at index i, the runtime for a doubly
      linked list would be O(n). However, if you do that same opperation on a Python list
      the runtime would be constent. Therefore, even though they are similar they are not the 
      same thing.
'''
'''
    7. Now that you've implemented linked lists and doubly-linked lists, you have the option
    of using these in place of python lists insisde your implementaiton of stacks, queues,
    and dekes. For each of these, explain which type of list
    (python lists, linked list, or doubly-linked list) shoudl give the best Big Oh runbning time
    in a comment.

    - For most projects that I have been a part of a Python list has been sufficent enough for what
      we needed. However, I can see a linked list or a doubly linked list being very usefull.
      If you're project needed to be as optomized as much as it can you are only going to be inserting
      data into collections a doubly linked list would be a great fit. Both data types would also be useful
      if you needed more control over your collection and wanted to keep that data collection/minuplation appstract
      from the main project.
'''

# Used to test Stack
def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

# Used to test Queue
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

# Used to test Dequeue
def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

def testLinkedList():
    li = Linked_List()
    li.add(48)
    li.add(50)
    li.add(23)
    li.remove(50)
    li.printList()
    print('Search for 50: ', li.search(50))
    print('Search for 40: ', li.search(48))
    print('isEmpty: ', li.isEmpty())
    print('Size: ', li.size())
    li.append(63)
    print('Index of 23: ', li.index(23))
    li.insert(2, 777)
    li.add(4)
    li.add(1)
    li.add(2)
    print('Last Pop: ', li.pop())
    print('Pos Pop of index 1: ', li.pop(1))
    li.printList()

def testDoubly():
    li = Doubly_Linked()
    li.add(7)
    li.add(5)
    li.add(90)
    li.remove(5)
    li.printList()
    print('Search for 50: ', li.search(5))
    print('Search for 40: ', li.search(90))
    print('isEmpty: ', li.isEmpty())
    print('Size: ', li.size())
    li.append(63)
    print('Index of 23: ', li.index(23))
    li.insert(2, 777)
    li.add(4)
    li.add(1)
    li.add(2)
    print('Last Pop: ', li.pop())
    print('Pos Pop of index 1: ', li.pop(1))
    li.printList()

def main():
    print('\nTesting Stack: Convert 4749 to binary: ')
    print(divideBy2(4749))
    print('\nTesting Queue Hot Potato: ')
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
    print('\nTesting Dequeue')
    print('Testing lsdkjfskf:', palchecker("lsdkjfskf"))
    print('Testing radar:', palchecker("radar"))
    print('\nTesting Linked List: ')
    testLinkedList()
    print('Testing Doubly Linked List: ')
    testDoubly()

main()

def main():
    # mylist = Linked_List()
    # mylist.add(31)
    # mylist.add(77)
    # mylist.add(17)
    # mylist.add(93)
    # mylist.add(26)
    # mylist.add(54)

    # print(mylist.size())
    # print(mylist.search(93))
    # print(mylist.search(100))

    li = Doubly_Linked()
    li.add(15)
    li.add(55)
    li.add(27)
    li.add(97)

    li.remove(55)
    
    print(li)

if __name__ == "__main__":
    main()