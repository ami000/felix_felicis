from operator import itemgetter


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self, key):
        hsh = 0
        for char in key:
            hsh += ord(char)
        return hsh % self.MAX

    def __getitem__(self, key):
        h = self.getHash(key)
        listAtH = self.arr[h]
        for element in listAtH:
            if element[0] == key:
                return element[1]
        # else:
        #     raise Exception('Not Found')

    def __delitem__(self, key):
        h = self.getHash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

    def __setitem__(self, key, value):
        # self.arr[self.getHash(key)]  = value
        h = self.getHash(key)

        found = False

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))


if __name__ == '__main__':
    table  = HashTable()
    table['march 6'] = 120
    table['march 6'] = 78
    table['march 8'] = 67
    table['march 9'] = 4
    table['march 17'] = 459
    print(table.arr)
    del table['march 17']
    print(table.arr)
    print(table['march 6'])
    print(table['march 17'])
    table['march 17'] = 459
    print(list(zip(*table.arr[9])))
    # table.__setitem__('1st June', 12345)
    # print(table.__getitem__('1st June'))
    # print(table.__getitem__('1 June, 21:30'))