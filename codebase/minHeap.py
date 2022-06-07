class MinHeap:
    def __init__(self, capacity):
        self.array = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get_parent_index(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        return self.get_parent_index(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def getParent(self, index):
        return self.array[self.get_parent_index(index)]

    def getLeftChild(self, index):
        return self.array[self.getLeftChildIndex(index)]

    def getRightChild(self, index):
        return self.array[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]

    def insert(self, data):
        if self.isFull():
            raise Exception('Heap is full')
        self.array[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)

    def heapifyUp(self, index):
        if self.hasParent(index) and self.getParent(index) > self.array[index]:
            self.swap(self.get_parent_index(index), index)
            self.heapifyUp(self.get_parent_index(index))

    def heapifyDown(self, index):
        smallest = index
        if self.hasLeftChild(index) and self.array[smallest] > self.getLeftChild(index):
            smallest = self.getLeftChildIndex(index)
        if self.hasRightChild(index) and self.array[smallest] > self.getRightChild(index):
            smallest = self.getRightChildIndex(index)
        if smallest != index:
            self.swap(index, smallest)
            self.heapifyDown(smallest)
        # while self.hasLeftChild(index):
        #     smallerChildIndex = self.getLeftChildIndex(index)
        #     if self.hasRightChild() and self.getRightChild(index) < self.getLeftChild(index):
        #         smallerChildIndex = self.getRightChildIndex(index)
        #
        #     if self.array[index] < self.array[smallerChildIndex]:
        #         break
        #     else:
        #         self.swap(index, smallerChildIndex)
        #     index = smallerChildIndex


    def removeMin(self):
        if self.size == 0:
            raise Exception('Empty Heap')
        data = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return data
