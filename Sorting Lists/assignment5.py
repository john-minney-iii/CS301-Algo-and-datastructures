

'''
    CS301 - Algo and Data Struc
    Assignment 5 | Sorting Lists
    John Minney
    4/1/2021
'''

def selection_sort(li):
    # Loop through the list backwards since we are going to insert at the end
    for i in range(len(li)-1, -1, -1):
        max_index = i

        # Loop through the numbers behind the current index i
        for j in range(i-1, -1, -1):
            if li[max_index] < li[j] : max_index = j
            
        # Swap the max_index and the current index
        li[i], li[max_index] = li[max_index], li[i]

def selection_sort_test():
    print("\nTesting Selection Sort ------------------------------")
    print("\nNormal List of Numbers:")
    li = [7,5,6,9,120,23,45,63,214,56,36,787,10,236,10,11,26,-5,-36,-5]
    print('\tBefore Sort:', li)
    selection_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------
    print('\nList of Negative Number:')
    li = [-5, -36, -202, -1101, -5654, -9696, -32541, -1, -2, -354, -6, -66]
    print('\tBefore Sort:', li)
    selection_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------
    print('\nList of Only 1 Item')
    li = [7]
    print('\tBefore Sort:', li)
    selection_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------
    print('\nEmpty List')
    li = []
    print('\tBefore Sort:', li)
    selection_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------
    print('\nList of the Same Number:')
    li = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print('\tBefore Sort:', li)
    selection_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------
    print('\nList of Strings')
    li = ["hi", "apple", "computer", "laptop", "test", "debug", "program", "python"]
    print('\tBefore Sort:', li)
    selection_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------

# ============================================================================================

def merge_sort(li):
    # This fails if the list is only 1 element.. so just check for it
    if len(li) > 1:
        mid = len(li)//2
        # The list needs to be split into two sections. From the middle
        left_side  = li[:mid]
        right_side = li[mid:]
        # Recursive Call both Sides
        merge_sort(left_side)
        merge_sort(right_side)
        # Now we need to "merge" together the two sides to be in order
        # Take the initial index of all the lists
        left_index = right_index = 0
        merged_index = 0
        # Originaly I was going to user For Loops... but since we have two different
        # index values a while loop will let us keep track of both of these
        while left_index < len(left_side) and right_index < len(right_side):
            if left_side[left_index] <= right_side[right_index]:
                li[merged_index] = left_side[left_index]
                left_index += 1
            else:
                li[merged_index] = right_side[right_index] 
                right_index += 1
            merged_index += 1
        # The above code won't place all of the values back into the original list...
        # So you have to have an extra to place the remaning code
        # For loops won't work here either... because we used a while loop for the loops
        # above and we were increasing a variable to keep track of our index we have to use 
        # a while loop to continue using that index that we were last at
        while left_index < len(left_side):
            li[merged_index] = left_side[left_index]
            left_index += 1 
            merged_index += 1

        while right_index < len(right_side):
            li[merged_index] = right_side[right_index]
            right_index += 1
            merged_index += 1

def merge_sort_test():
    print("\nTesting Merge Sort ------------------------------")
    print("\nNormal List of Numbers:")
    li = [7,5,6,9,120,23,45,63,214,56,36,787,10,236,10,11,26,-5,-36,-5]
    print('\tBefore Sort:', li)
    merge_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------
    print('\nList of Negative Number:')
    li = [-5, -36, -202, -1101, -5654, -9696, -32541, -1, -2, -354, -6, -66]
    print('\tBefore Sort:', li)
    merge_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------
    print('\nList of Only 1 Item')
    li = [7]
    print('\tBefore Sort:', li)
    merge_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------
    print('\nEmpty List')
    li = []
    print('\tBefore Sort:', li)
    merge_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------
    print('\nList of the Same Number:')
    li = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print('\tBefore Sort:', li)
    merge_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------
    print('\nList of Strings')
    li = ["hi", "apple", "computer", "laptop", "test", "debug", "program", "python"]
    print('\tBefore Sort:', li)
    merge_sort(li)
    print('\tAfter Sort: ', li)
    # --------------------------------------------------------------------------

def main():
    selection_sort_test()
    print('\n======================================================================================================')
    merge_sort_test()
    
if __name__ == '__main__':
    main()