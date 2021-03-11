
# Assignment 4
# Katie Williams
# John Minney
# 3/9/2021

# https://github.com/john-minney-iii/CS301-Algo-and-datastructures/tree/master/CS301-Assignment-4

def search_sorted_list(sorted_list, item):
	return _rec_search(sorted_list, 0, len(sorted_list), item)

def _rec_search(list, low, high, item):
	if high >= low:
		mid = (high + low)//2
		if list[mid] == item  : return True
		else:
			if item > list[mid] : return _rec_search(list, mid+1, high, item)
			elif item < list[mid] : return _rec_search(list, low, mid-1, item)
	else:
		return False

class HashList:
        def __init__(self, length):
                self.cap = length
                self.size = 0
                self.slots = [None] * self.cap

        '''
                For both best and worst case hashfunction runs at
                constant time. O(1)
        '''
        def hashfunction(self, item):
                return item % self.cap

        '''
            For best case put runs at constant time (O(1)) because
            you already have the index of where you want to place the item.
            For worst case it runs at linear time O(n). With n being
            the size of slots.
        '''
        def _solve_collision(self, slot, item): # Linear Helper Method
                temp = slot
                currSlot = self.slots[temp]
                while currSlot is not None:
                        if temp == self.cap-1 : temp = 0
                        else : temp += 1
                        currSlot = self.slots[temp]
                return temp

        def put(self, item):
                if self.size == self.cap : raise Exception('HashList is Full.')
                else:
                        slot = self.hashfunction(item)
                        if self.slots[slot] is not None:
                                new = self._solve_collision(slot, item)
                                self.slots[new] = item
                                self.size += 1
                        else:
                                self.slots[slot] = item
                                self.size += 1

        '''
            For best case contains runs at constant time (O(1)) because
            you already have the index of the item.
            For worst case it runs at linear time O(n). With n being
            the size of slots.
        '''
        def _hide_and_seek(self, slot, item): # Linear Helper Method
                temp = slot
                currSlot = self.slots[temp]
                while currSlot is not None:
                        if currSlot == item : return True
                        else:
                                if temp == self.cap-1 : temp = 0
                                else:
                                        if temp == slot - 1 : break
                                        else:
                                                temp += 1
                                                currSlot = self.slots[temp]
                if currSlot is None : return False

        
        def contains(self, item):
                slot = self.hashfunction(item)
                if self.slots[slot] == item : return True
                else:
                        return self._hide_and_seek(slot, item)

        '''
                For both best and worst case items
                runs at constant time. O(1)
        '''
        def items(self):
                return self.slots

        '''
                To convert the HashList to work as a dictionary, you would have
                to modify the hashfunction to incorporate keys instead of the
                modulo division. 
        '''

def binary_search_test():
        print('Binary Search Test Case ---------------')
        li = [9841, 65, 21, 9, 5, 3, 7, 82, 42]
        li.sort()
        print(*li, sep=', ')
        print('Search for 42:', search_sorted_list(li, 42))
        print('Search for 99:', search_sorted_list(li, 99))

def hashlist_test():
        print('HashList Test Case ---------------')
        hash = HashList(10)
        print(hash.items())
        hash.put(14)
        print(hash.items())
        hash.put(4)
        print(hash.items())
        hash.put(9)
        print(hash.items())
        hash.put(19)
        print(hash.items())
        hash.put(199)
        print(hash.items())
        print(hash.contains(5))
        print(hash.contains(4))
        print(hash.contains(199))
        

def main():
        binary_search_test()
        hashlist_test()
	
	

if __name__ == '__main__':
	main()
