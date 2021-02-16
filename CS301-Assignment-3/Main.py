from Stack import Stack
from Queue import Queue
from Deque import Deque

'''
    Used to test the Stack Data Class

    @Param num to be converted
    @Return binary version of num
'''
def binaryConverter(num) -> str:
    stack = Stack()

    while num > 0:
        stack.push(num % 2)
        num = num // 2

    binStr = ''
    while not stack.isEmpty():
        binStr += str(stack.pop())
    return binStr

'''
    Used to test the Queue Data Class

    @Param list of names and a num to loop with
    @Return name that lost
'''
def hotPotato(names, num) -> str:
    queue = Queue()
    for name in names:
        queue.enqueue(name)

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

'''
    Used to test the Deque Data Class

    @Param string to test if palindrome
    @Return bool if param is palindrome
'''
def palchecker(aString) -> str:
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

def main():
    print(binaryConverter(345))
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
    print(palchecker("lsdkjfskf"))
    print(palchecker("radar"))

if __name__ == "__main__":
    main()