class  Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

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
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

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

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def reverse(self):
        itr = self.head
        prev = None

        while itr:
            # print('Old itr:', itr.data if itr is not None else None)
            next = itr.next
            prev = itr.prev
            # print('Old next:', next.data if next is not None else None)
            # print('Old prev:', prev.data if prev is not None else None)
            itr.next = prev
            # print('New next:', itr.next.data if itr.next is not None else None)
            itr.prev = next
            # print('New prev:', prev.data if prev is not None else None)
            itr = next
            # print('New itr:', itr.data if itr is not None else None)
        if prev is not None:
            self.head = prev.prev
if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    # ll.print_backward()
    # ll.insert_at_end("figs")
    # ll.print_forward()
    # ll.insert_at(0, "jackfruit")
    # ll.print_forward()
    # ll.insert_at(2, "kiwi")
    # ll.print_forward()
    ll.reverse()
    ll.print_forward()