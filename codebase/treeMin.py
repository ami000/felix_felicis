import math
import unittest

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# iterative
def treeMinDftI (root: TreeNode):
    if root is None: return 0
    stack = [root]
    lowest = math.inf
    while len(stack) > 0:
        curr = stack.pop()
        if curr.data: lowest = min(lowest, curr.data)
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return lowest

def treeMinBftI (root: TreeNode):
    if root is None: return 0
    q = [root]
    lowest = math.inf
    while len(q) > 0:
        curr = q.pop(0)
        lowest = min(lowest, curr.data)
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    return lowest

# recursive

def treeMinDftR (root:TreeNode):
    if root is None: return math.inf
    return min(root.data, treeMinDftR(root.left), treeMinDftR(root.right))

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
        # self.assertEqual(1, treeMinDftI(root))  # add assertion here
        # self.assertEqual(1, treeMinBftI(root))  # add assertion here
        self.assertEqual(1, treeMinDftR(root))  # add assertion here
        self.assertEqual(math.inf, treeMinDftR(None))


if __name__ == '__main__':
    unittest.main()
