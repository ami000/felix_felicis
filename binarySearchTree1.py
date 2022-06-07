class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add to left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit root/base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        # visit root/base node
        elements = [self.data]

        # visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.post_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()

        # visit root/base node
        elements.append(self.data)
        return elements

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        return sum(self.in_order_traversal())

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is  None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        return self


def buildTree (elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child((elements[i]))
    return root

def pre_order_traversal(root):
    # visit root/base node
    elements = [root.info]

    # visit left tree
    if root.left:
        elements += root.left.pre_order_traversal()

    # visit right tree
    if root.right:
        elements += root.right.pre_order_traversal()
    return elements
if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbersBST = buildTree(numbers)
    print(numbersBST.in_order_traversal())
    numbersBST.delete(17)
    print(numbersBST.in_order_traversal())

    # print(numbersBST.search(21))
    # print(numbersBST.find_min())
    # print(numbersBST.find_max())
    # print(numbersBST.calculate_sum())
    print(numbersBST.pre_order_traversal())
    # print(numbersBST.post_order_traversal())
