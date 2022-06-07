import unittest

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# iterative
def treeSumDftI (root: TreeNode):
    if root is None: return 0
    stack = [root]
    total = 0
    while len(stack) > 0:
        curr = stack.pop()
        total += curr.data
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return total

def treeSumBftI (root: TreeNode):
    if root is None: return 0
    q = [root]
    total = 0
    while len(q) > 0:
        curr = q.pop(0)
        total += curr.data
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    return total

# recursive

def treeSumDftR (root:TreeNode):
    if root is None: return 0
    return root.data + treeSumDftR(root.left) + treeSumDftR(root.right)

def buildTree():
    a = TreeNode(3)
    b = TreeNode(11)
    c = TreeNode(4)
    d = TreeNode(4)
    e = TreeNode(2)
    f = TreeNode(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a

class MyTestCase(unittest.TestCase):
    def test_something(self):
        root  = buildTree()
        # self.assertEqual(25, treeSumDftI(root))  # add assertion here
        self.assertEqual(25, treeSumBftI(root))  # add assertion here
        self.assertEqual(25, treeSumDftR(root))  # add assertion here
        self.assertEqual(0, treeSumDftR(None))


if __name__ == '__main__':
    unittest.main()
