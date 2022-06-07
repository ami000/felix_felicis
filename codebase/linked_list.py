class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node  = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def replace_with_values(self, data_list):
        self.head = None
        for value in data_list:
            self.insert_at_end(value)

    def insert_values(self, data_list):
        for value in data_list:
            self.insert_at_end(value)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head

        while itr.next:
            if itr.data == data:
                itr.next = itr.next.next
            itr = itr.next

    def getNth(self, index):
        itr = self.head  # Initialise temp
        count = 0  # Index of current node

        # Loop while end of linked list is not reached
        while itr:
            if count == index:
                return itr.data
            count += 1
            itr = itr.next
        # if we get to this line, the caller was asking
        # for a non-existent element, so we assert fail
        assert False
        return 0

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        linkedlistStr = ''
        while itr:
            linkedlistStr += str(itr.data) + '--->'
            itr = itr.next
        print(linkedlistStr)

    def reverse(self):
        prev = None
        itr = self.head

        while itr:
            # print('Old itr:', itr.data if itr is not None else None)
            next = itr.next
            # print('Old next:', next.data if next is not None else None)
            # print('Old prev:', prev.data if prev is not None else None)

            itr.next = prev
            # print('New next:', itr.next.data if itr.next is not None else None)
            prev = itr
            # print('New prev:', prev.data if prev is not None else None)
            itr = next
            # print('New itr:', itr.data if itr is not None else None)

        self.head = prev

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    # ll.print()
    # ll.insert_after_value("mango", "apple")  # insert apple after mango
    # ll.print()
    # ll.remove_by_value("orange")  # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    ll.reverse()
    ll.print()