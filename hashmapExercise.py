from operator import itemgetter

rangeFromWeek = {
    1: (1, 8),
    2: (8, 15),
    3: (15, 22),
    4:  (22, 31)
}

numberOfDaysByMonth = {
    'Jan' : 31,
    'Feb' : 28,
    'Mar' : 31,
    'Apr' : 30,
    'May' : 31,
    'Jun' : 30,
    'Jul' : 31,
    'Aug' : 31,
    'Sep' : 30,
    'Oct' : 31,
    'Nov' : 30,
    'Dec' : 31
}

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

    def getAverageForWeek(self, weekNumber):
        # print(rangeFromWeek(weekNumber))
        rangeF = rangeFromWeek[weekNumber]
        week1Temperatures = [self.__getitem__(f'Jan {i}') for i in range(rangeF[0], rangeF[1])]
        return sum(week1Temperatures) / len(week1Temperatures)

    def getMaxOfNDays(self, n):
        # print(rangeFromWeek(weekNumber))
        nTemperatures = [(f'Jan {i}', self.__getitem__(f'Jan {i}')) for i in range(1, n + 1) ]
        return max(nTemperatures, key=lambda item: item[1])[0]
        # return sum(week1Temperatures) / len(week1Temperatures)


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
    table['Jan 1'] = 27
    table['Jan 2'] = 31
    table['Jan 3'] = 23
    table['Jan 4'] = 34
    table['Jan 5'] = 37
    table['Jan 6'] = 38
    table['Jan 7'] = 29
    table['Jan 8'] = 30
    table['Jan 9'] = 35
    table['Jan 10'] = 30
    print(table.getAverageForWeek(1))
    print(table.getMaxOfNDays(10))
    # print(list(zip(*table.arr)))
    # table.__setitem__('1st June', 12345)
    # print(table.__getitem__('1st June'))
    # print(table.__getitem__('1 June, 21:30'))