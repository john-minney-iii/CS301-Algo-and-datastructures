
# Assignment 4
# 3/9/2021

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
        def __init__(self):
                pass

        def hashfunction(item):
                pass

        def put(item):
                pass

        def contains(item):
                pass

        def items():
                pass


def main():
	li = [9841, 65, 21, 9, 5, 3, 7, 82, 42]
	li.sort()
	print(*li, sep=', ')
	print('Search for 42:', search_sorted_list(li, 42))
	print('Search for 99:', search_sorted_list(li, 99))

if __name__ == '__main__':
	main()
