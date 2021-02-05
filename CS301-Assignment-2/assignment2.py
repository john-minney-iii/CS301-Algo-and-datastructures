
# John Minney III
# CS301-Assignment-2
# 2/2/2021

import time
from random import randrange

#---------------------------------------------------------

class CSVFile:

    csv_file = None

    def __init__(self, file_name):
        self.csv_file = open(file_name, 'w+')

    def write_list_header(self):
        self.csv_file.write('List Size, Benchmark\r')

    def write_dict_header(self):
        self.csv_file.write('Dict Size, Benchmark\r')

    def write_line(self, line):
        self.csv_file.write(line)

    def close_file(self):
        self.csv_file.close()

# List Test ----------------------------------------------

class ListTest:

    def start_tests(self):
        print('Starting List Tests')
        self.test_different_sizes('list_append.csv', self.list_append)
        self.test_different_sizes('list_end_del.csv', self.list_delete_end)
        self.test_different_sizes('list_middle_add.csv', self.list_middle_add)
        self.test_different_sizes('list_middle_del0.csv', self.list_middle_del)
        self.test_different_sizes('list_start_add.csv', self.list_start_add)
        self.test_different_sizes('list_start_del.csv', self.list_start_del)
        self.test_different_sizes('list_in.csv', self.is_in_list)
        print('Done Testing Lists')

    # Util -------------------------------------------------
    def bench_mark(self, funct, li):
        t1 = time.time()
        ans = funct(li)
        t2 = time.time()
        return t2-t1

    def generate_list(self, size):
        return [i for i in range(size)]

    def generate_list_sizes(self):
        return [ self.generate_list(i) for i in range(999999, 5000001, 100000) ]

    # Func to Test ------------------------------------------
    def list_append(self, li):
        li.append(777)

    def list_delete_end(self, li):
        del li[-1]

    def list_middle_add(self, li):
        li.insert(len(li)//2, 777)

    def list_middle_del(self, li):
        del li[len(li)//2]

    def list_start_add(self, li):
        li.insert(0, 777)

    def list_start_del(self, li):
        del li[0]

    def is_in_list(self, li):
        return 500 in li # I choose to do a const value

    # Testing Code ----------------------------------------------
    def test_lists(self, funct, li):
        bench = self.bench_mark(funct, li)
        return str(len(li)) + ',' + str(bench) + '\r'

    def test_different_sizes(self, csv_name, funct):
        print('\tCreating ' + csv_name + '...')
        sizes = [i for i in range(999999, 20000001, 1000000) ]
        csv_file = CSVFile(csv_name)
        csv_file.write_list_header()
        for size in sizes:
            csv_file.write_line(self.test_lists(funct, self.generate_list(size)))
        csv_file.close_file()
        print('\t' + csv_name + ' done.')

# Dict Tests -----------------------------------------------------

class DictTests:

    def start_tests(self):
        print('Started Dictionary Tests...')
        self.test_different_sizes('dict_add.csv', self.dect_add)
        self.test_different_sizes('dict_del.csv', self.dect_del)
        self.test_different_sizes('dict_in.csv', self.is_in_dict)
        print('Done Testing Dictionary.')

    def start_in(self):
        self.test_different_sizes('dict_in.csv', self.is_in_dict)

    # Util -----------------------------------------
    def bench_mark(self, funct, li):
        t1 = time.time()
        ans = funct(li)
        t2 = time.time()
        return t2-t1

    def generateDict(self, size):
        tempDict = {}
        for i in range(size):
            tempDict[i] = i
        return tempDict
    
    # Func to Test ---------------------------------
    def dect_add(self, di):
        di['a'] = 1

    def dect_del(self, di):
        del di[1] # every dictionary will have a key of 1

    def is_in_dict(self, di):
        return (len(di) // 2) in di #Looks for the element in the middle

    # Testing Code ---------------------------------
    def test_dict(self, funct, di):
        bench = self.bench_mark(funct, di)
        return str(len(di)) + ',' + str(bench) + '\r'

    def test_different_sizes(self, csv_name, funct):
        print('\tCreated ' + csv_name + '...')
        sizes = [i for i in range(999999, 50000001, 1000000) ]
        csv_file = CSVFile(csv_name)
        csv_file.write_dict_header()
        for size in sizes:
            csv_file.write_line(self.test_dict(funct, self.generateDict(size)))
        csv_file.close_file()
        print('\t' + csv_name + ' done.')

# ----------------------------------------------------------------

def main():

    listTest = ListTest()
    listTest.start_tests()
    
    dictTest = DictTests()
    dictTest.start_tests()
    

if __name__ == "__main__":
    main()